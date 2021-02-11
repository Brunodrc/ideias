def main():
    inicio = apresentação()    
    tip_tabuada = int(input('Digite o tipo de tabuada que deseja mostrar: '))
    
    while tip_tabuada != 5:
        if tip_tabuada == 1:
            n = int(input("Digite um número: "))
            print(f"A tabuada de multiplicação do número {n} é a seguinte:")
            tmultiplicação = tabuada_multiplicar(n)
        
        elif tip_tabuada == 2:
            n = int(input("Digite um número: "))
            print(f"A tabuada de divisão do número {n} é a seguinte:")
            tdivisao = tabuada_dividir(n)
        
        elif tip_tabuada == 3:
            n = int(input("Digite um número: "))
            print(f"A tabuada de adição do número {n} é a seguinte:")
            tadicao = tabuada_adicionar(n)
        
        elif tip_tabuada == 4:
            n = int(input("Digite um número: "))
            print(f"A tabuada de subtração do número {n} é a seguinte:")
            tsubtracao = tabuada_subtrair(n)
        
        inicio = apresentação()
        tip_tabuada = int(input('Digite o tipo de tabuada que deseja mostrar: '))
    
    print('programa encerrado. Obrigado por usar nosso programa') 
        
    

def apresentação():
    opcoes = '~~~~~~~~ veja as tabuadas de 1 à 10 ~~~~~~~~\n'
    opcoes += 'Escolha o tipo de tabuada:\n'
    opcoes += '[1] para tabuada de multiplicação\n'
    opcoes += '[2] para tabuada de divisão\n'
    opcoes += '[3] para tabuada de adição\n'
    opcoes += '[4] para tabuada de subtração\n'
    opcoes += '[5] para encerrar o programa\n'
    
    print(opcoes)
    

def tabuada_multiplicar(valor):
    for i in range(1,11):
        print(f"{valor} x {i} = {valor * i}")

def tabuada_dividir(valor):
    for i in range(1,11):
        multiplo = valor * i 
        print(f"{multiplo} / {valor} = {multiplo / valor:.0f}")

def tabuada_adicionar(valor):
    for i in range(1,11):
        print(f'{valor} + {i} = {valor + i}')

def tabuada_subtrair(valor):
    for i in range(valor,11+valor):
        print(f'{i} - {valor} = {i - valor}')

if __name__=='__main__':
    main()