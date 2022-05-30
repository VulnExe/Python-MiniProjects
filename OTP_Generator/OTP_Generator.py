import random
generatorotp=random.randint(000000,100000)
username=input("username:")
print('hello..!',username)
print('here is your otp for login',generatorotp)
password=input("enter the otp to login")
if password==str(generatorotp):
    print('login success')
else:

    print('login failed')