#!/bin/bash

# Change the variable IP to whichever ip address and port number you 
# want the server to run from
IP='192.168.1.18:8000'

source ~/Virt/bin/activate
cd ledpi
./manage.py runserver $IP
