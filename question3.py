# name=input("enter the password:-")
# if len(name)>=6 and len(name)<=16:
#     if "$" in name:
#         if "2" or "8" in name:
#             if "A" or "Z" in name:
#                 print("strong password ")
#             else:
#                 print("weak password")
#         else:
#             print("weak password")
#     else:
#         print("weak password")
# else:
#     print("weak password")




name=input("enter the number:-")
a=[]
b=[]
c=[]
d=[]
for i in (name):
    if i=="@" or i=="#" or i=="$":
        a.append(i)
    elif i>="A" and i<="Z":
        b.append(i)
    elif i>="a" and i<="z":
        c.append(i)
    elif i>"0" and i<"9":
        d.append(i)
print("speshal character",a)
print("capetel letter",b)
print("smol letter",c)
print("number",d)
print("strong password")




