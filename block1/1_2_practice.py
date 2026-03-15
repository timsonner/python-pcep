#import pdb; pdb.set_trace()
import random

def get_classful_subnet(octet):
    if octet & 0b10000000 == 0: return "A"
    if octet & 0b11000000 == 0b10000000: return "B"
    if octet & 0b11100000 == 0b11000000: return "C"
    if octet & 0b11110000 == 0b11100000: return "D"
    return "E"

first_octet = random.randrange(1,255,1)
second_octet = random.randrange(1,255,1)
third_octet = random.randrange(1,255,1)
fourth_octet = random.randrange(1,255,1)

print("IP:",end=" ")
print(first_octet,second_octet,third_octet,fourth_octet,sep=".")
print(f"{first_octet:08b}.{second_octet:08b}.{third_octet:08b}.{fourth_octet:08b}")
print(f"Class: {get_classful_subnet(first_octet)}")


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

