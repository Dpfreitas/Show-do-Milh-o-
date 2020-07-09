
from random import choice
from time import time
from sys import exit

#--------------------------------------------------------------------------------------------------------------

print('------------------')
print('SHOW DO MILHÃO')
print('------------------')

#--------------------------------------------------------------------------------------------------------------

def inicio():
    global k
    global v
    global q
    global u
    global c
    global z
    global q
    global j
    global a
    global b

    a = 0
    b = 0
    z = 0
    v = a + b + z
    c = 1
    e = 0
    u = 0
    p = 0
    q = 0
    j = 0
    k = 0
    print('INSTRUÇÕES: UTILIZE O CAPSLOCK LIGADO PARA DIGIRTAR AS \nLETRAS (S) PARA SIM E (N) PARA NÃO . \nAO DIGITAR AS RESPOSTAS , DIGITE NÚMEROS DE 1 A 9 ! ')
    print()
    print('VOCÊ POSSUI 40 SEGUNDOS PARA RESPONDER CADA PERGUNTA !')
    print()
    print('BOM JOGO!')
    print()

    x = str(input('CASO QUEIRA COMEÇAR , DIGITE S :'))
    if x == 'S':
        x=choice([1,2,3,4,5,6,7,8,9,10,11])
        if x == 1:
            p1()
        elif x == 2:
            p2()
        elif x == 3:
            p3()
        elif x==4:
            p4()
        elif x==5:
            p5()
        elif x==6:
            p6()
        elif x==7:
            p7()
        elif x==8:
            p8()
        elif x==9:
            p9()
        elif x==10:
            p10()
        elif x==11:
            p11()
    else:

        inicio()

#--------------------------------------------------------------------------------------------------------------

def denovo():
    x=str(input('Caso queira jogar de novo , digite S :'))
    if x == 'S':
        inicio()

#---------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------

def turno():
    global v
    global a
    global b
    global z
    global c
    global e
    v = a + b + z
    n = c + e
    if n <= 5:
        a = c*1000
        print('-------------------')
        print('VALENDO R$1.000,00 ')
        print('-------------------')
        print('Você possui ->R$',v,',00')
        print('------------------------')

    elif 5 < n <= 10:
        a=0
        b= (c-5)*10000
        print('-------------------')
        print('VALENDO R$10.000,00')
        print('-------------------')
        print('Você possui ->R$', v, ',00')
        print('------------------------')

    elif 10 < n <= 15:
        a=0
        b=0
        z = (c-10)*100000
        print('--------------------')
        print('VALENDO R$100.000,00')
        print('--------------------')
        print('Você possui ->R$', v, ',00')
        print('------------------------')



def milhão():
    global v
    global c

    if c==16:
        v = 1000000
        print('----------------------')
        print('VALENDO R$1.000.000,00')
        print('----------------------')
        x=choice([1,2,3,4])
        if x == 1:
            pm1()
            denovo()
        elif x == 2:
            pm2()
            denovo()
        elif x == 3:
            pm3()
            denovo()
        elif x==4:
            pm4()
            denovo()


# --------------------------------------------------------------------------------------------------------------



a=0
b=0
z=0
v=a+b+z
c=0
e=0
u=0
p=0
q=0
j=0
k=0
#--------------------------------------------------------------------------------------------------------------

def p1():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('----------------------------------------')
    print('Qual é o nome dado ao estado da água em forma de gelo?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)LÍQUIDO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)SÓLIDO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)GASOSO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)VAPOROSO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0=time()
    r1()#alterar na proxima pergunta
    t1=time()
    dt=t1-t0
    if dt>=40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')


    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt<40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p2()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        c = 1
        print('VOCE GANHOU R$', v, ',00!')
        denovo()

def r1():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x == 9:
        k=1

    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r1()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r1()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p2()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r1()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r1()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r1()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r1()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r1()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r1()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r1()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r1()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p2():
    global k
    global v
    global q
    global u
    global c
    global e
    turno()
    milhão()
    print('p2')
    print('----------------------------------------')
    print('Qual é o país do tango?')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('1)URUGUAI')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('2)ESPANHA')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('3)PARAGUAI')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('4)ARGENTINA')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r2()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40 and k==0:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1 and k==0:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p3()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1 :
        c=1
        print('VOCE GANHOU R$', v, ',00!')
        denovo()


def r2():
    global k
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x == 9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r2()
    if x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r1()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p3()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q >= 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r2()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r2()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r2()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r2()#alterar na proxima pergunta
    if x == 5:
        if u == 0:
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            u = u + 1
            r2()  # alterar na proxima pergunta

        else:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r2()  # alterar na proxima pergunta
    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r2()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 2 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            r2()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p3():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p3')
    print('----------------------------------------')
    print('Em qual país está localizado o “Muro das lamentações”??')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('1)ALEMANHA')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('2)BRASIL')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('3)VENEZUELA')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('4)ISRAEL')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r3()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40 and k==0:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1 and k==0:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p4()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()


def r3():
    global k
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x== 9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,4,4,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')

        r3()

    if  x == 8:
        if p == 1 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r4()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p4()
    if x == 7:
        z = 0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r2()  # alterar na proxima pergunta
        else:
            q = q + 1
            z = choice([1, 2, 3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r3()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r3()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r3()#alterar na proxima pergunta
    if x == 5:
        if u == 0:
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            u = u + 1
            r1()  # alterar na proxima pergunta

        else:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r1()  # alterar na proxima pergunta
    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r3()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 2 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            r3()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p4():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p4')
    print('----------------------------------------')
    print('Quem é a namorada do Mickey?')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('1)MARGARIDA')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('2)MINNIE')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('3)A PEQUENA SEREIA')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('4)OLÍVIA PALITO')  # alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r4()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40 and k==0:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1 and k==0:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p5()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()


def r4():
    global k
    global q
    global p
    global u
    global e
    global c
    print('----------------------------------------')
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    print('----------------------------------------')
    if x == 9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')

        r4()
    if x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r4()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p5()#alterar na proxima pergunta
    if x == 7:
        z = 0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r2()  # alterar na proxima pergunta
        else:
            q = q + 1
            z = choice([1, 2, 3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r4()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r4()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r4()#alterar na proxima pergunta
    if x == 5:
        if u == 0:
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u = u + 1
            r1()  # alterar na proxima pergunta

        else:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r1()  # alterar na proxima pergunta
    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r4()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r4()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p5():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p5')
    print('----------------------------------------')
    print('Como é chamado quem nasce em Milão, na Itália?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)MILANSENSE')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)MILANOSO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)MILISTA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)MILANÊS')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r5()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p6()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r5():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 4,4,4,4,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r5()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r5()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p5()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r5()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r5()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r5()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r5()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r5()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r5()#alterar na proxima pergunta

    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r5()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 2 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            r5()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p6():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p6')
    print('----------------------------------------')
    print('Onde nasceu Van Gogh, o grande pintor impressionista?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)POLÕNIA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)FRANÇA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)ITÁLIA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)HOLANDA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r6()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p7()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r6():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x == 9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,4,4,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r6()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r6()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p7()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r6()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r6()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r6()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r6()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r6()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r6()#alterar na proxima pergunta

    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r6()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 2 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            r6()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p7():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p7')
    print('----------------------------------------')
    print('Fidel Castro nasceu em que país?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)JAMAICA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)CUBA')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)EL SÁLVADOR')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)México')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r7()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p8()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r7():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,3,2,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r7()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r7()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p8()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r7()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r7()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r7()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r7()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r7()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r7()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r7()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r7()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p8():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p8')
    print('----------------------------------------')
    print('Em qual estádio Pelé marcou seu milésimo gol?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)MORUMBI')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)PACAEMBU')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)MARACANÂ')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)MINEIRÃO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r8()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p9()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r8():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,3,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r8()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r8()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p9()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r8()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r8()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r8()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r8()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r8()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r8()#alterar na proxima pergunta

    if x == 3:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r8()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r8()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p9():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p9')
    print('----------------------------------------')
    print('O que significa literalmente Perestroika?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)CONVERSÃO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)INVOLUÇÃO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)REESTRUTURAÇÃO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)REGRESSÃO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    t0 = time()
    r9()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p10()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r9():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,3,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r9()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r9()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p10()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r9()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r9()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r9()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r9()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r9()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r9()#alterar na proxima pergunta

    if x == 3:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r9()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r9()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p10():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p10')
    print('----------------------------------------')
    print('Quem é o patrono do exército brasileiro?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)MARECHAL DEODORO')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)BARÃO DE MAUÁ')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)DUQUE DE CAXIAS')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)MARQUÊS DE POMBAL')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r10()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p11()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r10():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 3,3,3,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r10()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r10()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p11()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r10()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r10()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r10()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r10()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r10()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r10()#alterar na proxima pergunta

    if x == 3:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r10()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r10()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p11():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p11')
    print('----------------------------------------')
    print('Em que estado brasileiro nasceu a apresentadora xuxa?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Rio de Janeiro')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Rio Grande do Sul')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Santa Catarina')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Goiás')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r11()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p12()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r11():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r11()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r10()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p12()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r11()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r11()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r11()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r11()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r11()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r11()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r11()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r11()#alterar na proxima pergunta

#--------------------------------------------------------------------------------------------------------------

def p12():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p12')
    print('----------------------------------------')
    print('Que imperador pôs fogo em Roma?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Trajano')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Nero')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Brutus')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Calígula')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r12()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p13()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r12():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r12()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r12()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p13()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r12()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r12()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r12()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r12()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r12()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r12()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r12()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r12()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p13():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p13')
    print('----------------------------------------')
    print('Qual oceano tem o maior volume de água?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Atlântico')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Pacífico')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Indico')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Ártico')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r13()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p14()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r13():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,2,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r13()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r13()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p14()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r13()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r13()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r13()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r13()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r13()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r13()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r13()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r13()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p14():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p14')
    print('----------------------------------------')
    print('Quem foi o grande amor de Julieta?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Romeu')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Orfeu')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Hamlet')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Iago')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r14()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p15()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r14():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,1,1,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r14()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r14()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p15()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r14()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r14()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r14()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r14()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r14()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r14()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r14()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 1)')
        else:
            r14()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p15():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p15')
    print('----------------------------------------')
    print('Como eram chamados os pilotos suicidas da Segunda Guerra?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Camicases')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Sashimis')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Haraquiris')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Sumôs')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r15()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p16()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r15():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,1,1,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r15()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r15()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p16()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r15()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r15()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r15()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r15()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r15()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r15()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r15()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 1)')
        else:
            r15()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p16():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p16')
    print('----------------------------------------')
    print('Que conflito ideológico envolveu os EUA e a União Soviética?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Guerra Fria')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Guerra do Vietnã')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Guerra nas Estrelas')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Guerra da Coréia')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r16()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p17()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r16():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,1,1,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r16()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r16()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p17()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r16()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r16()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r16()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r16()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r16()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r16()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r16()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r16()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p17():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p17')
    print('----------------------------------------')
    print('Como se chama o lugar onde são armazenadas as balas de um revólver?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1) Cano')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Tambor')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Agulha')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Gatilho')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r17()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p18()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()

def r17():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r17()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r17()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p18()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r17()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r17()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r17()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r17()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r17()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r17()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r17()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r17()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p18():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p18')
    print('----------------------------------------')
    print('Peroba é uma espécie de?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1) Inseto')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Árvore')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Verme')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Verdura')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r18()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p19()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r18():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r18()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r18()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p19()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r18()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r18()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r18()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r18()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r18()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r18()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r18()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r18()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p19():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p19')
    print('----------------------------------------')
    print('Qual produto gerou guerras e conflitos no século XX?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1) Álcool')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Petróleo')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Ouro')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Alumínio')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r19()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p20()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r19():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r19()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r19()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p20()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r19()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r19()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r19()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r19()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r19()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r19()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r19()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r19()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p20():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p20')
    print('----------------------------------------')
    print('Qual personagem da turma da Mônica tem apenas cinco fios de cabelo?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1) Mônica')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Cebolinha')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Cascão')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Magali')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r20()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p21()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r20():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r20()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r20()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p21()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r20()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r20()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r20()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r20()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r20()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r20()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r20()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r20()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p21():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p21')
    print('----------------------------------------')
    print('O Coliseu é um monumento histórico de que cidade européia?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1) Paris')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Copenhahue')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Roma')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Londres')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r21()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p22()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r21():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 3,3,3,3,3,3,3,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r21()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r21()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p22()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r21()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r21()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',1,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r21()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r21()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r21()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r21()#alterar na proxima pergunta

    if x == 3:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r21()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r21()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p22():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p22')
    print('----------------------------------------')
    print('A eletrônica é parte de qual ciência?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Física')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Biologia')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Química')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Botânica')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r22()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p23()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r22():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,1,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r22()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r22()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p23()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r22()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r22()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r22()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',3)#alterar na proxima pergunta
            print('----------------------------------------')
            r22()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r22()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r22()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r22()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 3)')
        else:
            r22()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p23():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p23')
    print('----------------------------------------')
    print('O churrasco é considerado uma comida típica de qual estado?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Ceará')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Rio Grande do Sul')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Pará')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Maranhão')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r23()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p24()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r23():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,1,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r23()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r23()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p24()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r23()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r23()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r23()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r23()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r23()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r23()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r23()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r23()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p24():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p24')
    print('----------------------------------------')
    print('Qual é a moeda oficial da Alemanha?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Lira')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Março')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Franco')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Libra')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r24()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p25()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r24():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,4,3,1,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r24()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r24()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p25()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r24()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r24()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r24()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r24()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 3')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r24()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r24()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r24()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r24()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p25():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p25')
    print('----------------------------------------')
    print('A Bélgica é:')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Uma república')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Uma monarquia constitucional')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Um emirado')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Um principado')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r25()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p26()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r25():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,4,3,1,2,1,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r25()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r25()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p26()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r25()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r25()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r25()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r25()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r25()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r25()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r25()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r25()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p26():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p26')
    print('----------------------------------------')
    print('Qual é o nome dado ao pneu reserva do carro?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Calota')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Estepe')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Macaco')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Chave de roda')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r26()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p27()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r26():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 2,2,2,2,2,2,2,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r26()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r26()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p27()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r26()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r26()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r26()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r26()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 2')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r26()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r26()#alterar na proxima pergunta

    if x == 2:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r26()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 2)')
        else:
            r26()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p27():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p27')
    print('----------------------------------------')
    print('Que planta era usada para fabricação de papel no antigo Egito?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Papiro')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Eucalipto')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Oliveira')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Milho')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r27()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 - t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p28()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r27():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,1,1,2,3,1,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r27()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r27()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p28()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r27()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r27()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r27()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r27()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r27()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r27()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r27()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 1)')
        else:
            r27()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p28():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p28')
    print('----------------------------------------')
    print('A união do espermatozóide com o óvulo origina uma célula chamada:')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Zigoto')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Bigoto')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Feto')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Garoto')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')
    t0 = time()
    r28()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p29()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r28():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,1,1,1,2,3,1,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r28()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r28()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p29()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r28()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r28()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r28()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r28()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r28()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r28()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r28()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 1)')
        else:
            r28()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p29():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p29')
    print('----------------------------------------')
    print('Qual é o nome do cachorro medroso do Salsicha, dosdesehos animados?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Floquinho')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Rin-tin-tin')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Lassie')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Scooby-doo')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r29()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p30()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r29():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE :4,4,4,4,4,4,4,4,1,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r29()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r29()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p30()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r29()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            r29()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r29()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r29()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r29()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r29()#alterar na proxima pergunta

    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r29()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            r29()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def p30():
    global k
    global v
    global q
    global u
    global c
    global e
    milhão()
    turno()
    print('p30')
    print('----------------------------------------')
    print('Que país europeu tem como atração a tourada?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Espanha')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Itália')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)França')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Alemanha')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0 = time()
    r30()  # alterar na proxima pergunta
    t1 = time()
    dt = t1 -t0
    if dt >= 40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')

    if k == 0 and e == 0 and dt < 40:
        print('-------------------------------------------------------------------')
        a = str(input('CASO QUEIRA CONTINUAR , DIGITE S , CASO CONTRÁIO DIGITE N :'))
        print('-------------------------------------------------------------------')
        if a == 'S':
            p31()
        if a == 'N':
            print('VOCE GANHOU R$', v, ',00!')
    if k == 1:
        print('VOCE GANHOU R$', v, ',00!')
        denovo()
def r30():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if  x==9:
        k=1
    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE :4,4,4,4,4,4,4,4,1,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        r30()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r30()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            p31()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r30()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            r30()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',3,',',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r30()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            r30()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')  # alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            r30()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            r30()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('CERTA RESPOSTA!')
        else:
            r30()#alterar na proxima pergunta
    elif x == 1 or x == 2 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 1)')
        else:
            r30()#alterar na proxima pergunta

#-------------------------------------------------------------------------

def pm1():
    global k
    global v
    global q
    global u
    global c
    global e
    turno()
    print('----------------------------------------')
    print('Na criação do Estado do Tocantins, que estado teve o território reduzido?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Goiás')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Mato Grosso')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Pará')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Maranhão')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0=time()
    rm1()#alterar na proxima pergunta
    t1=time()
    dt=t1-t0
    if dt>=40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')



    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$0,00!')
        print('----------------------------------------')


    if k == 1:
        c = 1
        print('VOCE GANHOU R$', v, ',00!')
        denovo()

def rm1():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x == 9:
        k=1

    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 1,1,1,3,3,4,4,3,2,2 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        rm1()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            r1()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            pm2()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm1()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',4)#alterar na proxima pergunta
            print('----------------------------------------')
            rm1()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            rm1()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            rm1()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 1')#alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            rm1()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm1()#alterar na proxima pergunta

    if x == 1:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('---------------------------')
            print('CERTA RESPOSTA!')
            print('VOCÊ GANHOU R$1.000.000,00')
            print('PARABÉNS!!!!')
            print('----------------------------')
        else:
            rm1()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 1)')
        else:
            rm1()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def pm2():
    global k
    global v
    global q
    global u
    global c
    global e
    turno()
    print('----------------------------------------')
    print('Que nome recebe a foz de um rio que se abre para o mar?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Alagado')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)Manguezal')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Pântano')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)Estuário')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0=time()
    rm2()#alterar na proxima pergunta
    t1=time()
    dt=t1-t0
    if dt>=40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')



    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$0,00!')
        print('----------------------------------------')


    if k == 1:
        c = 1
        print('VOCE GANHOU R$', v, ',00!')
        denovo()

def rm2():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x == 9:
        k=1

    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 4,4,3,4,4,3,2,2,4,4 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        rm2()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            rm2()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            pm3()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm2()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            rm2()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            rm2()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            rm2()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')#alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            rm2()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm2()#alterar na proxima pergunta

    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('---------------------------')
            print('CERTA RESPOSTA!')
            print('VOCÊ GANHOU R$1.000.000,00')
            print('PARABÉNS!!!!')
            print('----------------------------')
        else:
            rm2()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            rm2()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def pm3():
    global k
    global v
    global q
    global u
    global c
    global e
    turno()
    print('----------------------------------------')
    print('Em que ano Ayrton Senna venceu o primeirocampeonato de Fórmula 1?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)1987')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)1990')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)1985')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)1988')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0=time()
    rm3()#alterar na proxima pergunta
    t1=time()
    dt=t1-t0
    if dt>=40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')



    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')


    if k == 1:
        c = 1
        print('VOCE GANHOU R$0,00!')
        denovo()

def rm3():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x == 9:
        k=1

    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 4,4,3,4,4,3,2,2,4,4 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        rm3()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            rm3()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            pm4()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm3()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            rm3()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            rm3()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            rm3()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')#alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            rm3()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm3()#alterar na proxima pergunta

    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('---------------------------')
            print('CERTA RESPOSTA!')
            print('VOCÊ GANHOU R$1.000.000,00')
            print('PARABÉNS!!!!')
            print('----------------------------')
        else:
            rm3()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            rm3()#alterar na proxima pergunta

#--------------------------------------------------------------------------

def pm4():
    global k
    global v
    global q
    global u
    global c
    global e
    turno()
    print('----------------------------------------')
    print('Qual é a menor República do mundo?')#alterar na proxima pergunta
    print('----------------------------------------')
    print('1)Mônaco')#alterar na proxima pergunta
    print('----------------------------------------')
    print('2)San Marino')#alterar na proxima pergunta
    print('----------------------------------------')
    print('3)Nova Zelândia')#alterar na proxima pergunta
    print('----------------------------------------')
    print('4)China')#alterar na proxima pergunta
    print('----------------------------------------')
    print('5)UNIVERSITÁRIOS')
    print('----------------------------------------')
    print('6)PLATÉIA')
    print('----------------------------------------')
    print('7)CARTAS')
    print('----------------------------------------')
    print('8)PULO')
    print('----------------------------------------')
    print('9)PARO')
    print('----------------------------------------')

    t0=time()
    rm4()#alterar na proxima pergunta
    t1=time()
    dt=t1-t0
    if dt>=40:
        e=0
        print('Resposta inválida , tempo esgotado !')
        print('----------------------------------------')
        print('VOCÊ GANHOU R$', v, ',00!')
        print('----------------------------------------')



    if e >= 1:
        v = v / 2
        print('----------------------------------------')
        print('VOCÊ GANHOU R$0,00')
        print('----------------------------------------')


    if k == 1:
        c = 1
        print('VOCE GANHOU R$', v, ',00!')
        denovo()

def rm4():
    global k
    global j
    global q
    global p
    global u
    global e
    global c
    x = int(input('DIGITE O NÚMERO DA RESPOSTA :'))
    if x == 9:
        k=1

    if  x == 6:
        print('------------------------------------------------------')
        print("A PLATEIA DIZ QUE : 4,4,3,4,4,3,2,2,4,4 ESTÃO CORRETAS")
        print('------------------------------------------------------')
        rm4()

    if  x == 8:
        if p == 3 :
            print('----------------------------------------')
            print('VOCE NÃO PULAR MAIS DO QUE 3 PERGUNTAS')
            print('----------------------------------------')
            rm4()#alterar na proxima pergunta
        else:
            p=p+1
            print('----------------------------------------')
            print('Pulando uma pergunta...')
            print('===============================================')
            pm1()#alterar na proxima pergunta
    if x == 7:
        z=0
        if q == 1:
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm4()  # alterar na proxima pergunta
        else:
            q=q+1
            z=choice([1,2,3])
        if z == 3:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3,',',1)#alterar na proxima pergunta
            print('----------------------------------------')
            rm4()#alterar na proxima pergunta
        if z == 2:
            print('----------------------------------------')
            print('alternativas excluidas -->',2,',',3)#alterar na proxima pergunta
            print('----------------------------------------')
            rm4()#alterar na proxima pergunta
        if z == 1:
            print('----------------------------------------')
            print('alternativa excluida -->',2)#alterar na proxima pergunta
            print('----------------------------------------')
            rm4()#alterar na proxima pergunta
    if x == 5:
        if u == 0 :
            print('----------------------------------------')
            print('UNIVERSITÁRIO 1 --> ALTERNATIVA 2')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 2 --> ALTERNATIVA 3')#alterar na proxima pergunta
            print('----------------------------------------')
            print('UNIVERSITÁRIO 3 --> ALTERNATIVA 4')#alterar na proxima pergunta
            print('----------------------------------------')
            u=u+1
            rm4()#alterar na proxima pergunta

        else :
            print('---------------------------------------------------------')
            print('ESSA AJUDA JÁ FOI SOLICITADA , ESCOLHA OUTRA ALTERNATIVA.')
            print('---------------------------------------------------------')
            rm4()#alterar na proxima pergunta

    if x == 4:
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            c=c+1
            print('---------------------------')
            print('CERTA RESPOSTA!')
            print('VOCÊ GANHOU R$1.000.000,00')
            print('PARABÉNS!!!!')
            print('----------------------------')
        else:
            rm4()#alterar na proxima pergunta
    elif x == 1 or x == 3 or x == 4 :
        print('----------------------------------------')
        y = str(input('ESTÁ CERTO DISSO ? SIM(S) OU NÃO(N) :'))
        print('----------------------------------------')
        if y == 'S':
            e=e+1
            print('RESPOSTA ERRADA , ALETERNATIVA CORRETA --> 4)')
        else:
            rm4()#alterar na proxima pergunta

#--------------------------------------------------------------------------
inicio()
denovo()
