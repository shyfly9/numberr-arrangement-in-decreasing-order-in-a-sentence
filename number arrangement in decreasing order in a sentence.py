string=input()
n=[]
s=[]
f=[]
num=""
word=""
for i in string:
    if i.isdigit():
        num = num+i 
        if word!="":
            s.append(word)
            f.append(word)
            word=""
    else:
        word=word+i 
        if num!="":
            n.append(int(num))
            f.append(int(num))
            num=""

if len(string)==len(word):
    print(word)
elif len(string)==len(num):
    print(num)
else:
    
    if word!="":
        s.append(word)   
    if num!="":
        n.append(int(num))
    
    n.sort(reverse=True)

    if str(f[0]).isdigit():
        r=""
        k=0
        for i in n:
            r = r+str(i)
            if k<len(s):
                r=r+s[k]
                k=k+1
    else:
        r=""
        k=0
        for i in s:
            r = r+i
            if k<len(n):
                r=r+str(n[k])
                k=k+1
    
    print(r)
