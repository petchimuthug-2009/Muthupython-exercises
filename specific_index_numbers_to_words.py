q=[]
a=['0','1','2','3','4','5','6','7','8','9']
b=['zero','one','two','three','four','five','six','seven','eight','nine']
a1=int(input('enter the initial value'))
a2=int(input('enter the final value'))
b1=[str(i) for i in range(a1,a2+1)]
d=len(b1)
print(d)
i=0
f=int(input('enter the index which  you want to convert:'))
while i<d:
    p=list(b1[i])
    for j in range(0,10):
        if p[f] == a[j]:
            p[f]=b[j]
            r=''.join(p)
            q.append(r)
            
            j+=1
    i+=1
print(q)
