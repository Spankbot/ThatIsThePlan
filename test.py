from sys import exit
import time

#An introduction.
print "\t\t\tTHAT IS THE PLAN \nLet's start with your name."

#An easy way to tell where are you.
def locationsign(location):
 print "\n\t~~~---===(You are in %s)===---~~~\n" % location
 
 
def start():
#Starting room
 locationsign("your home")
 print '''
 You are on your sofa,listening a weird music.
 You are came exhausted from your work 
 and the only thing you want to do is relax.
 You hear your telephone ringing.
 '''
 prompt = raw_input("> ")
 
 
 
 
def name():
# Asks the user if he wants to change the name or not.
 print "Do you want to change your name?"
 option = raw_input("Yes/No: ")
 
 option = option.lower()
 
 if option == "yes":
  print "Write your name:"
  name_char = raw_input("> ")
   
 elif option == "no":
  print "Alright,let's start then."
   
 else:
  while option != "yes" or "no":
   print "Please enter Yes or No"
   name()
     
name()
start()


