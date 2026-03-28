# Task: Use print() with sep= and end= parameters. Get user input and cast to int/float.

"""
Program that reads the /etc/services file and prints each line without adding an extra newline. Then, read the /etc/passwd file and print only the usernames separated by commas.

example output:
service1
service2
service3
username1,username2,username3,
"""

with open("/etc/services", "r") as services:
    for service in services:
        print(service,end="")
services.close()

with open("/etc/passwd", "r") as passwd:
    for line in passwd:
        username = line.split(":")[0]
        print(username,end=",",sep=":")