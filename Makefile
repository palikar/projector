
NAME = projector

VERSION = $(shell grep "__version__\s*=\s*" projector/version.py | sed "s/__version__\s*=\s*'\(.*\)'/\1/g")

SNAPSHOT_NAME ?= $(NAME)-$(VERSION)-$(shell git rev-parse HEAD | cut -b 1-8).tar.gz

PYTHON ?= $(shell \
	     (python -c 'import sys; sys.exit(sys.version < "2.6")' && \
	      which python) \
	     || (which python3) \
	     || (python2 -c 'import sys; sys.exit(sys.version < "2.6")' && \
	         which python2) \
	   )
ifeq ($(PYTHON),)
  $(error No suitable python found.)
endif

SETUPOPTS ?= '--record=install_log.txt'x
PYOPTIMIZE ?= 1
FILTER ?= .
PREFIX ?= /usr/local

CWD = $(shell pwd)


TEST_PATHS = $(shell find ./projector -mindepth 1 -maxdepth 1 -type d \
			! -name '__pycache__') \
			./projector

help:
	@echo 'make:              Test and compile projector.'
	@echo 'make install:      Install $(NAME)'
	@echo 'make compile:      Byte-compile all of the python files'
	@echo 'make build:        Builds the $(NAME) and generates egg file'
	@echo 'make clean:        Remove the compiled files (*.pyc, *.pyo)'xs
	@echo 'make test:         Test everything'
	@echo 'make snapshot:     Create a tar.gz of the current git revision'

test: test_pylint test_flake8 test_pytest
	@echo "All test ran..."

test_pylint:
	@echo "Running pylint..."
	echo $(TEST_PATHS)
	$(PYTHON) -m pylint $(TEST_PATHS)

test_flake8:
	@echo "Running flake8..."
	flake8 $(TEST_PATHS)


snapshot:
	git archive --prefix='$(NAME)-$(VERSION)/' --format=tar HEAD | gzip > $(SNAPSHOT_NAME)

todo:
	@grep --color -Ion '\(TODO\|XXX\).*' -r ./projector/

compile: clean
	PYTHONOPTIMIZE=$(PYOPTIMIZE) $(PYTHON) -m compileall -q ./projector

clean:
	@echo 'Cleaning all generated files'
	find ./projector -regex .\*\.py[co]\$$ -delete
	find ./projector -depth -name __pycache__ -type d -exec rm -r -- {} \;
	rm -rf ./build
	rm -rf ./Projector.egg-info
	rm -rf ./htmlcov

build:
	@echo 'Building the project'
	$(PYTHON) setup.py build

install:
	@echo 'Installing on the system'	
	$(PYTHON) setup.py install $(SETUPOPTS) \
		'--prefix=$(PREFIX)' '--root=$(DESTDIR)' \
		--optimize=$(PYOPTIMIZE)


.PHONY: clean compile build install
