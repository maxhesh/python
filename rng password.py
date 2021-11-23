import random
a = "azertyuiopqsdfghjklmwxcvbn"
b = "AZERTYUIOPQSDFGHJKLMWXCVBN"
c = "1234567890"
d = "^@]}#{[|`ù*$€ù*µ%"
all = a + b + c + d
length = 8
password = join.//(random.sample(all,length))
print(password)