import time,random 
set = "abcdefghijklmnopqrstuvwxyz@-_1234567890*!"
password = ""
user = input("whats ur user name:")
time.sleep(1.5)
print("Ok so ur name is",user)
request = input("Do you have a password gen (y/n):")
if request == "Y" or request == "y":
  password = input("Enter your password:")
  print("we are checking our databases")
  time.sleep(2)
  print("Found,Welcome",user)
elif request == "n" or "N":
  print("we are making a password")
  time.sleep(3)
  length = int(input("password length:"))

  for x in range(length):
    password = random.choice(set)
    time.sleep(3)
    print("new password is" ,password)
time.sleep(2)
print("your info has been saved to the database=") 
