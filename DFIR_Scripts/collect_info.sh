#!/bin/bash
cd /
mkdir -p ECH_investigations
cd ECH_investigations
echo "#################################" > information.txt
date >> information.txt
echo "Investigator: " >> information.txt
echo "..............." >> information.txt
echo "#################################" >> information.txt
echo "Hostname: " >> information.txt
hostname >> information.txt
echo "Username: " >> information.txt
who >> information.txt
echo "---------------------------------" >> information.txt
echo "Operating System: " >> information.txt
cat /etc/os-release >> information.txt
echo "---------------------------------" >> information.txt
echo "Running Processes: " >> information.txt
pstree >> information.txt
echo "---------------------------------" >> information.txt
echo "Network Connections: " >> information.txt
sudo netstat -tupn >> information.txt
#if netstat is not installed and not want to install it.
#sudo ss -tuln >> information.txt
echo "---------------------------------" >> information.txt
echo "Disk Details: " >> information.txt
sudo df >> information.txt
echo "---------------------------------" >> information.txt
