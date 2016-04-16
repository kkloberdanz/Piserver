#!/bin/bash
cd ~
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install python3-pip 
sudo pip3 install virtualenv
mkdir Virt/
virtualenv Virt/ -p python3
source ~/Virt/bin/activate
pip3 install -r requirements.txt
