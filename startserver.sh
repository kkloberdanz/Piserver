#!/bin/bash
source ~/Virt/bin/activate
cd ledpi
./manage.py runserver 192.168.1.18:8000
