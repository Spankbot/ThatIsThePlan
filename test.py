from sys import exit
import time



def name():
# Asks the user if he wants to change the name or not.
 print "Do you want to change your name?"
 option = raw_input("Yes/No:")
 
 while option != "Yes" or "No":
  if option == "Yes":
   print "Write your name:"
   name_char = raw_input("> ")
   
  elif option == "No":
   print "Alright,let's start then."
   
  else:
   print "Please enter Yes or No"
   option = 
     
name()
