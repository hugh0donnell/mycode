#!/usr/bin/env python3
ipchk = input("Enter an IP address: " ) 

# a string tests as True
if ipchk == "192.168.70.1":
    print("IP address given matched preset: " + ipchk + "  Bad idea.")
elif ipchk:
    print("Looks like the IP address was set: " + ipchk)
else: 
    print("No IP provided.")


