#!/usr/bin/python3
 
import requests
import os
import sys
import time
import urllib
import random
 
auth_data = ('admin', 'your_password_replace_it')
 
# Create random IP tests
ip_to_blackhole = "127.0.0.%d" % random.randint(1,254)
 
print "Blackhole IP:", ip_to_blackhole

# Encode any values which have spaces or '/' inside them
ip_to_blackhole = urllib.quote_plus(ip_to_blackhole)

r = requests.put('http://127.0.0.1:10007/blackhole/' + ip_to_blackhole, auth=auth_data)
 
if r.status_code == 200:
    print "Correctly blackholed IP"
else:
    print "Can't add new subnet", r.json()['error_text']

print "Wait 5 second to propagate changes"
time.sleep(5)

# Show all blocked hosts
r = requests.get('http://127.0.0.1:10007/blackhole', auth=auth_data)
 
if r.status_code != 200:
    print "API call failed", r.json()["error_text"]
    sys.exit(0)
 
# Let's find UUID for this IP address
blocked_hosts = r.json()["values"]

blackhole_uuid = ""

for host in blocked_hosts:
    if host["ip"] == ip_to_blackhole + "/32":
        blackhole_uuid = host["uuid"] 

if blackhole_uuid == "":
    print "Can't find UUID for blackholed host"
    sys.exit(0)
else:
    print "Correctly found UUID for this IP", blackhole_uuid


r = requests.delete('http://127.0.0.1:10007/blackhole/' + blackhole_uuid, auth=auth_data)
 
if r.status_code != 200:
    print "Cannot delete blackhole announce"
    sys.exit(0)
else:
    print "Correctly removed blackhole announce"
    sys.exit(0)
