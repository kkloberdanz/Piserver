#!/bin/bash

# Change the variable IP to whichever ip address and port number you 
# want the server to run from
#IP='172.17.87.191:8000'

# Get's hosts IP address, if it doesn't work, then comment this out,
# and uncomment the line below that says 'IP='192.168...''
IP=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')

#IP='192.168.1.18'
PORT=':8000'


source ~/Virt/bin/activate
cd ledpi
./manage.py runserver $IP$PORT
