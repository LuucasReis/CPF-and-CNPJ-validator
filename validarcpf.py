def validarcpf1(cpf):

    if not cpf.isnumeric():
        return "Isso não é um numero! Tente novamente."
    elif len(cpf) != 11:
        return"Quantidade de números insuficientes para um CPF! Tente novamente."
       

    p1 = 0
    CPF_n= cpf[:-2]

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
    if cpf[-2] == d1 and cpf[-1] == d2:
        for i,n in enumerate(cpf):
            if i == 3 or i == 6:
                f_CPF+="."+ n
            elif i == 9:
                f_CPF+="-"+ n
            else:
                f_CPF+= n
            
        return f"O CPF {f_CPF} é válido!!"

    else:
        return f"O CPF {f_CPF} não é válido!!"

