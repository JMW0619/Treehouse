praise = ("you are doing great")
praise = praise.upper()
num_of_cha = len(praise)
result = praise + "!" * (num_of_cha // 2)
print(result)

advice1 = ("Don't forget to ask for help")
advice1 = advice1.upper()
num_of_cha = len(advice1)
result = advice1 + "!" * (num_of_cha // 2)
print(result)

advice2 = ("Don't Repeat Yourself. Keep Things DRY")
advice2 = advice2.upper()
num_of_cha = len(advice2)
result = advice2 + "!" * (num_of_cha // 2)
print(result)

#with the "def" function

def yell(text):
  text = text.upper()
  num_of_cha = len(text)
  result = text + "!" * (num_of_cha // 2)
  print(result)
  
yell("you are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep Things DRY")
