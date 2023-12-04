first_name = input("what is your first name?   ")

print("Hello", first_name)
if first_name == "Jay":
  print(first_name, "is learning Python")
elif first_name == "Haley":
  print(first_name, "should probably be careful coding on a PC")
else:
  age = int(input("How old are you?   "))
  if age <= 6:
    print("Wow you're {}! If you're confident with your reading already.")
  print("You should totally learn Python, {}!".format(first_name))
print("Have a great day {}!".format(first_name)) 
