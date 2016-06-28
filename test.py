from sys import exit
from items import *

#An introduction.
print "\t\t\tTHAT IS THE PLAN \nLet's start with your name."

#An easy way to tell where are you.
def locationsign(location):
#An easy way to tell where are you.
 print "\n\t~~~---===(You are in %s)===---~~~\n" % location
 
 
def start():
#Starting room
 locationsign("your home")
 print '''
 You are on your sofa,listening a weird music.
 You came exhausted from your work 
 and the only thing you want to do is relax.
 You hear your telephone ringing.
 '''
def start_options():
#The option tree
 prompt = raw_input("> ")
 prompt = prompt.lower()
 
 if prompt == "nothing":
  print "Are you really gonna do nothing?"
  start_options()
  
 elif prompt == "answer phone" or prompt == "pick up phone":
  print "You answer the phone.\n"
  print ''' It's your boss,he needs you to do extra hours.
 You,frustrated,stand up and told your boss to fuck off.
 Your boss tells you to remember the deal.
 Angry,told him that you're on your way.
 You grab your car keys and searched for a weapon.
 There's an AXE, a PISTOL and a KNIFE.
 What one do you choose?'''
  weapons = raw_input()
  weapons = weapons.lower
  
  while weapons != "axe" or weapons != "pistol" or weapons != "knife":
   print "I don't think there's one."
   weapons = raw_input()
   weapons = weapons.lower
  print "\nYou grab the %s." % prompt()
  
 else:
  while prompt != "nothing" or prompt != "answer phone":
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


