name = input("What's your name? ")

answer = input("Hey, {}, do you understand Python while loops?\n(Enter yes or no)".format(name))

while answer != 'yes':
  print("Ok, {}, while loops in Python repeat as long as certain Boolean conditions are met.".format(name))
  answer = input("Okay, {}, now do you understand python loops?\n (Enter yes or no)".format(name))
if answer == 'yes':
  print("That's great, {}, I'm pleased that you understand while loops now. That was getting repetitive.".format(name))
