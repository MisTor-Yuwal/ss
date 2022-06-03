from cgitb import text
from email import message
from http import client
import imp
import fbchat
from fbchat import *
from fbchat.models import *
from pyfiglet import *;
import sys;
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
text = "fb-boom"
cprint(figlet_format(text,font= "digital"),"blue")
print("press ctrl+c to quit")

username = str(input("enter your username:"))

password= str(input("enter you pass:"))
client = fbchat.Client(username,password)
name=  input("enter name of victim:")
friends = client.searchForUsers(name)
friend = friends[0]
message= input("enter your message:")
x=0
y =int(input("how many times?:"))
while x<y:
    sent = client.send(fbchat.models.Message(message),friend.uid)

    if sent:
        print("running...")

print("stopped..")
