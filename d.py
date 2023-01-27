# a=input(('Enter String : '))
# b=a.capitalize()
# c=b[-4:-1]
# print(c.split())



print("---------Welcome to Pizza Shop!-----------")
print('''S ->Small
L ->Large
M ->Medium
\n''')
a= input("What size pizza do you want? :  ").upper()
b= input("Do you want pepperoni? Y or N :  ").upper()
c= input("Do you want extra cheese? Y or N : ").upper()
#e=input("Do you wanna give Tip? Y or N : ").upper()
# bill = 0
# if size == 's':
#     bill += 15
# if size == 'm':
#     bill += 20
# if size == 'l':
#     Bill+=25

d= 0

if a== "S":
    d+= 15
elif a== "M":
    d+= 20
elif a== "L":
    d+= 25

if b== "Y":
    if a== "S":
        d+= 2
    else:
        d+= 3
        
if c== "Y":
    d+= 1
    
print(f"Your bill sir : {d}") 

