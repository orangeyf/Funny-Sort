import random
b=[5,2,3,7,9,11,66,267]
r=[]
while len(r)!=len(b):
    r=[]
    random.shuffle(b,random.random)
    for y in range(0,len(b)-1):
        if b[y]<=b[y+1]:
            r.append(b[y])
            if len(r)==len(b)-1:
                crap=True
                r.append(b[len(b)-1])
        else:
            continue
print(r)
#Copy and pasted from offline IDE.
