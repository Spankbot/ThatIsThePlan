from sys import exit
import time



def name():
# Asks the user if he wants to change the name or not.
 print "Do you want to change your name?"
 option = raw_input("Yes/No:")
 
 option = option.lower()
 
 while option != "yes" or "no":
  if option == "yes":
   print "Write your name:"
   name_char = raw_input("> ")
   exit()
   
  elif option == "no":
   print "Alright,let's start then."
   exit()
  else:
   print "Please enter Yes or No"
   name()
     
name()
