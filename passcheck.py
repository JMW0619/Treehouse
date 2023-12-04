import sys

MASTER_PASS = 'opensesame'
password = input("please enter the super secret password:   ")
attempt_count = 1
while password != MASTER_PASS:
  if attempt_count > 3:
    sys.exit("Too many invalid attempts")
  password = input("Invalid, try again:   ")
  attempt_count += 1
print("Welcome to secret town")
