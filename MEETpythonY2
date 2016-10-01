#!/bin/bash

old_pwd=$(pwd)
cd ~/
if [[ -e y2-venv ]]; then
    source ~/y2-venv/bin/activate
else
    sudo apt-get install virtualenv
    virtualenv -p $(which python3) y2-venv
    source ~/y2-venv/bin/activate
    pip install Flask==0.10
    pip install sqlalchemy==1.0
    pip install IPython==4.0
fi
cd $old_pwd
