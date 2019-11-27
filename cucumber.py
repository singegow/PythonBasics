#!/usr/bin/env python
# =====================================================================================================
# title           : getnetactrelease.py
# description     : This script is to fetch the all the netact releases from /etc/hosts/
# python_version  : 2.6.6
# =====================================================================================================

__author__ = 'Anitha Ramu(anitha.singegowda_ramu@nokia.com'
__version__ = "1.0.1"
__title__ = "getnetactrelease"

import json
import sys
import execute
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


def fetchip():
    with open("/root/cucumber/vars.json", "r") as read_file:
        data = json.load(read_file)
        print(data)

def passwd_less_conn(ip):
    command = "ssh -q " + vmname + " grep NetAct /etc/netact-release | awk -F\" - \" {'print $1\":\" $3'}"
    releases = execute.get_output(command).strip().split('\n')

def fetchnetactrelease():
    '''
    This method fetches all netact releases from /etc/netact-release file

    Parameters:-
    ------------
    None

    Returns:-
    ---------
    list
            returns the list of all netact releases
    '''
    netact_release = []
    vmname = "10.91.60.178"
    file_exists = "ssh -q " + vmname + " ls /etc/netact-release"
    if "/etc/netact-release" in file_exists:
        command = "ssh -q " + vmname + " grep NetAct /etc/netact-release | awk -F\" - \" {'print $1\":\" $3'}"
        releases = execute.get_output(command).strip().split('\n')
        for value in releases:
            netact_release.append(value.strip().split(':')[0].strip() + ":" + value.strip().split(':')[1].strip())
    logging.info("The netact_release is :" + str(netact_release) + " : ")
    return netact_release


output = fetchnetactrelease()
ip_address = fetchip()
