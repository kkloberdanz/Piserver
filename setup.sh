#!/bin/bash
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install python3 && sudo apt-get install python3-pip && sudo pip3 install -r requirements.txt && echo "Setup complete! Run ./startserver.sh to start the server"


