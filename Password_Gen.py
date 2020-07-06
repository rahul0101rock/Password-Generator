import random
import string
leng=int(input("Enter the length of password: "))
d=list(string.digits)
l=list(string.ascii_lowercase)
u=list(string.ascii_uppercase)
s=[':', '?', '.','(', ')','@', '#', '$', '%', '=''/','|', '~','>','*']
rd=random.choice(d)
rl=random.choice(l) 
ru=random.choice(u) 
rs=random.choice(s)
st=input("Strength of your Password\ns-Strong\nm-Medium\nw-Weak\n")
if st=='s':
  full=d+l+u+s
  npass=[ru,rd,rl,rs]
  for i in range(leng-5):
    npass.append(random.choice(full))
    random.shuffle(npass)
elif st=='m':
  full=d+l+u
  npass=[ru,rd,rl]
  for i in range(leng-4):
    npass.append(random.choice(full))
    random.shuffle(npass)
elif st=='w':
  full=d+l
  npass=[rd,rl]
  for i in range(leng-5):
    npass.append(random.choice(full))
    random.shuffle(npass)
print("\nYour Genrated Password is")
print(random.choice(ru)+''.join(npass))
