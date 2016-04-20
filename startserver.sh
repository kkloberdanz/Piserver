#!/bin/bash

# Programmer: Kyle KLoberdanz
#             This script runs the server from the current IP address
#             and port 8000.
#
#             Once the server starts, type:
#             IP_ADDRESS:PORT_NUMBER/piserver to view the webpage
#               

trap '{ echo "Cleaning up GPIO..." ; python3 gpiocleanup.py; exit 1; }' INT
echo 'Getting current IP address...'

# Get's hosts IP address, if it doesn't work, then comment this out,
# and uncomment the line below that says 'IP='192.168...''
IP=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')

# check if IP is not empty
if [ -z $IP ]
then
    echo "FAILED"
    echo "Uncomment the line IP='192.168.1.18', and write the"
    echo 'correct IP address'
    exit 1
fi


#IP='192.168.1.18'
PORT=':8000' 

echo 'DONE'
echo "Running server from $IP$PORT"

#echo 'Starting Virtual Environment...'
#source ~/Virt/bin/activate 
#echo 'DONE'

cd ledpi

echo ""
echo "*** Go to http://$IP$PORT/piserver/ to view the web page ***"
echo ""
echo "Starting server..."

python3 manage.py runserver $IP$PORT
