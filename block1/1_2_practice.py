# Task: Demonstrate the use of keywords, indentation, and comments.

"""
Program to generate a random IP address, print it in binary, and determine its classful subnet

example output:
IP: 1.2.3.4
00000001.00000010.00000011.00000100
Class: A
Subnet: 255.0.0.0
"""

#import pdb; pdb.set_trace()
import random

# Gets the classful subnet of an IP address based on the first octet
def get_classful_subnet(octet):
    if octet & 0b10000000 == 0: return "A"
    if octet & 0b11000000 == 0b10000000: return "B"
    if octet & 0b11100000 == 0b11000000: return "C"
    if octet & 0b11110000 == 0b11100000: return "D"
    return "E"

# Generate a random IP address
first_octet = random.randrange(1,255,1)
second_octet = random.randrange(1,255,1)
third_octet = random.randrange(1,255,1)
fourth_octet = random.randrange(1,255,1)

# Print the IP address in decimal and binary, and print the classful subnet
print("IP:",end=" ")
print(first_octet,second_octet,third_octet,fourth_octet,sep=".")
print(f"{first_octet:08b}.{second_octet:08b}.{third_octet:08b}.{fourth_octet:08b}")
print(f"Class: {get_classful_subnet(first_octet)}")

# Print the subnet mask based on the classful subnet
if get_classful_subnet(first_octet) == "A":
    print("Subnet: 255.0.0.0")
elif get_classful_subnet(first_octet) == "B":
    print("Subnet: 255.255.0.0")
elif get_classful_subnet(first_octet) == "C":
    print("Subnet: 255.255.255.0")
elif get_classful_subnet(first_octet) == "D":
    print("Multicast")
else:
    print("Experimental")

