n=[2,3,3,4,4]
num=[]
for i in n:
        if i not in num:
            num.append(i)
        else:
            num.remove(i)
print(num[0])
