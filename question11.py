

sentence="NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
b=[]
c=""
for i in sentence:
    if i==" ":
        b.append(c)
        c=""
    else:
        c+=i
b.append(c)
print(b)


