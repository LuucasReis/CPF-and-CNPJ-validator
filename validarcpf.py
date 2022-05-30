while True:
    CPF= input("Insira um CPF:")
    if not CPF.isnumeric():
        print("Isso não é um numero! Tente novamente.")
    elif len(CPF) != 11:
        print("Quantidade de números insuficientes para um CPF! Tente novamente.")
    else:
        break

p1 = 0
CPF_n= CPF[:-2]

for i,x in enumerate(range(10,1,-1)):
    p1+= int(CPF_n[i]) * x

ex_1= 11-(p1%11)

if ex_1 > 9:
    d1= 0
else:
    d1= ex_1

p2=0
for i,x in enumerate(range(11,2,-1)):
    p2 += int(CPF_n[i])* x

p2 += d1 * 2

d2 = 11-(p2%11)

d1,d2 = str(d1), str(d2)

f_CPF=""
if CPF[-2] == d1 and CPF[-1] == d2:
    for i,n in enumerate(CPF):
        if i == 3 or i == 6:
            f_CPF+="."+ n
        elif i == 9:
            f_CPF+="-"+ n
        else:
            f_CPF+= n
            
    print(f"O CPF {f_CPF} é válido!!")

else:
    print(f"O CPF {f_CPF} não é válido!!")

