n=int(input('Introdu numarul de linii  a matricei:'))
m=[]
if ((n>=2)and(n<=10)):
    for l in range(0,n):
        l=[]
        for x in range(0,n):
            x=int(input('Introdu elementele matricei:'))
            l.append(x)
        m.append(l)
    print(m)
s1diagprincipala=[]
for i in range(len(m)):
    for j in range(len(m[0])) :
        if i==j :
            s1diagprincipala.append(m[i][j])
print("Suma componentelor diagonalei principale este=",s1diagprincipala)
s2diagsecundara=[] 
for i in range(len(m)):
    for j in range(len(m[0])) :
        n=5
        if i+j==n-1:
            s2diagsecundara.append(m[i][j])
print("Suma componentelor diagonalei secundare este=",s2diagsecundara) 
s3susdprincipala=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        if i<j:
            s3susdprincipala.append(m[i][j])
print("Suma componentelor aflate mai sus de diagonala principala este=",s3susdprincipala)
s4subdprincipala=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        if i>j:
            s4subdprincipala.append(m[i][j])
print('Suma componentelor aflate mai jos de diagonala principala este=',s4subdprincipala)
s5susdsecundara=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        if i+j<n-1:
           s5susdsecundara.append(m[i][j])
print('Suma componentelor aflate mai sus de diagonala secundara este=',s5susdsecundara)
s6subdsecundara=[]
for i in range(len(m)):
    for j in range(len(m[0])):
        if i+j>n-1:
            s6subdsecundara.append(m[i][j])
print("Suma componentelor aflate mai jos de diagonala secundara este=",s6subdsecundara)
        