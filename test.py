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
def start_options():
 prompt = raw_input("> ")
 prompt = prompt.lower()
 
 if prompt == "nothing":
  print "Are you really gonna do nothing?"
  
  
 elif prompt == "answer phone":
  print "You answer the phone."
  exit()
  
 elif prompt == "get up":
  print "You got up of the sofa."
  exit()
  
 else:
  while prompt != "nothing" or "answer phone" or "get up":
   print "I don't know what that means."
   start_options()
 
 
 
 
def name():
# Asks the user if he wants to change the name or not.
 name_char = "Varik"
 
 print 'Your name is %s,do you want to change your name?' % name_char
 option = raw_input("Yes/No: ")
 option = option.lower()
 
 if option == "yes":
  print "Write your name:"
  name_char = raw_input("> ")
  print "Your name is \"%s\",are you sure?" % name_char
  confirm = raw_input()
  confirm = confirm.lower()
  if confirm == "no":
   name()
  elif confirm == "yes":
   print "Alright,let's start then."
   start()
   start_options()
  else:
   print "I don't know what do you mean."
   
   
 elif option == "no":
  print "Alright,let's start then."
  start()
  start_options()
 else:
  while option != "yes" or "no":
   print "Please enter Yes or No"
   name()
     
name()


