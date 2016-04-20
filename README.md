#Rpiserver

Ensure you have an internet connection in order for the setup to work


This program will run a webserver from your rasberry pi 


To get started, run
    './setup.sh' 

This will install the requirements, which are as follows:
    Django
    Python 3 
    Pip3

If the script for some reason fails, ensure django is installed by running
    sudo pip3 install django


Run this script as the user 'pi' NOT as root.


To start the server
    './startserver.sh' 


The server should use your current IP address, and will use port 8000
If there is some problem with getting the ip address, use a text editor 
such as vi to change the variable IP to be your machines ip address and 
the port number you want to use.


To view the webpage, go to the ip address and port that the server is 
broadcasting from, and append /piserver
Example:
    http://192.168.1.100:8000/piserver/


Admin login info
    Username: admin
    Password: defaultpassword


