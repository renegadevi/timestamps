#!/bin/bash

os=$(cat /etc/issue | grep '\n' | awk '{print $1, $2}')

if [[ ! $os == "Ubuntu 18.04" ]]
then
    echo "This script has not been tested nor is supported on your system."
    read -p "Are you sure you want to continue? [Y/n] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy] ]]
    then
        [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1
    fi
else

    echo
    echo "----- Installing Git and Pip"
    sudo apt install -y git python3-pip

    echo
    echo "----- Downloading Timestamps"
    git clone https://gitlab.com/renegadevi/timestamps.git timestamps-temp

    echo
    echo "----- Installing requirements"
    python3 -m pip install -r timestamps-temp/requirements.txt

    echo
    echo "----- Installing Timestamps"
    sudo cp -r timestamps-temp/timestamps /usr/share
    sudo cp timestamps-temp/timestamps.desktop /usr/share/applications

    echo
    echo "----- Clean up after install"
    rm -rf timestamps-temp

    echo
    echo "Done."
fi
