#!/bin/sh

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

if ! [ -d $HOME/.config/projector ]
then
    echo "Creating config dir $HOME/.config/projector"
    mkdir -p ${HOME}/.config/projector
fi
rm -rf "$HOME/.config/projector/*"
cp -r ${DIR}/data/* $HOME/.config/projector
