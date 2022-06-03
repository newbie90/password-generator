import string
import random

print("**Password Generator **")
print()
length = int(input('Enter password length: '))
all = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.sample(all,length))
print ('your password:', password)