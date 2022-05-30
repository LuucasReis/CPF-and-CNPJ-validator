def valida(cnpj):
    cnpj_c= tratar_cnpj(cnpj)
    cnpj_t= cnpj_c[:-2]
    v1= valida_1(cnpj_t)
    v2= valida_2(v1)
    #print(v2)
    #print("-"*10)
    #print(cnpj_c)
    if v2 == cnpj_c:
        return print(f"O cnpj {cnpj} é válido!!")
    else:
        return print(f"O Cnpj {cnpj} é inválido!!")

def valida_1(cnpj_1):
    c1 = cnpj_1[:5]
    t1=[int(c1[i])*x for i,x in enumerate(range(5,1,-1))]

    
    c2= cnpj_1[4:]
    t2=[int(c2[i])*x for i,x in enumerate(range(9,1,-1))]

    soma_t= sum(t1+t2)
    d1= (11-(soma_t % 11))
    if d1 > 9:
        d1 = 0
    return cnpj_1 + str(d1)

def valida_2(cnpj_2):
    c3= cnpj_2[:6]
    t3=[int(c3[i])*x for i,x in enumerate(range(6,1,-1))]
    
    
    c4= cnpj_2[5:]
    t4=[int(c4[i])*x for i,x in enumerate(range(9,1,-1))]
    
    sum_t2= sum(t3+t4)
    d2= 11-(sum_t2 % 11)
    if d2 > 9:
        d2=0
    return cnpj_2 + str(d2)
    
    

def tratar_cnpj(cnpj):
    cnpj= cnpj.replace ('/','')
    cnpj= cnpj.replace('.','')
    cnpj= cnpj.replace('-','')
    return cnpj
    

