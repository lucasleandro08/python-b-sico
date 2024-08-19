
#lista_de_dados = []
#def transformar_em_megabytes(tamanho_em_bytes: str) -> float:
    #return int(tamanho_em_bytes) / (2**10)**2


#with open('usuarios.txt', 'r') as arquivo:
    #for linha in arquivo:
        #linha = linha.strip()
        #usuario = linha[:15]
        #tamanho_em_disco = transformar_em_megabytes(linha[16:])
        #lista_de_dados.append((usuario, tamanho_em_disco))

#cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
#------------------------------------------------------------------------
#Nr.  Usuário        Espaço utilizado     % do uso
#'''

#with open('relatório.txt', 'w') as arquivo:
    #tamanho_total_consumido = sum([tamanho for _, tamanho in lista_de_dados])
    #media = tamanho_total_consumido / len(lista_de_dados)
    #arquivo.writelines(cabecalho)
    #for indice, dados in enumerate(lista_de_dados, start=1):
        #usuario, tamanho_em_disco = dados
        #arquivo.writelines(
            #f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB
            #f'{tamanho_em_disco/tamanho_total_consumido:>6.2%}\n')
    #arquivo.writelines('\n')
    #arquivo.writelines(
        #f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    #arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')

#::::::::: lista 3 ::::::::
#Exercicio 3
#x1=int(input("digite o primeiro numero:  \n"))
#x2=int(input("digite o segundo numero:  \n"))
#x3=int(input("digite o terceiro numero:  \n"))
#x4=int(input("digite o quarto numero:  \n"))
#soma=x1+x2+x3+x4
#media=soma/4
#print("a media dos numeros é: ",media)

#Exercicio 2
#vetorList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#i = 0
#while i < len(vetorList):
#print(vetorList[i])
#i = i + 1
#vetorListinv=vetorList[::-1]
#print(list (vetorListinv))

#Execicio 1
#vetorList = [1, 2, 3, 4, 5]
#i = 0
#while i < len(vetorList):
#print(vetorList[i])
#i = i + 1

#:::::::::::::::::::::::::::
#import statistics as stats
#notas=[]
#media=0
#for i in range(4):
# notas=float(input('informe uma nota: '))
#notas.append(notas)
#media= stats.mean(notas)
#print(f'Média = {media:.2f}')

#co = float(input('Entre com o valor do cateto oposto: '))
#ca = float(input('Entre com o valor do cateto adjacente: '))

#hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

#print("\n**************************\n")

#print("O valor da hipotenusa é: ",hipotenusa)

#def raizes(a, b, c):
#D = (b**2 - 4*a*c)
#x1 = (-b + D**(1/2)) / (2*a)
#x2 = (-b - D**(1/2)) / (2*a)

#print('\nValor de x1: {0}'.format(x1))
#print('Valor de x2: {0}'.format(x2))

#if __name__ == '__main__':
#while True:
#print('Calculando as raízes de uma equação de 2º grau\n')
#a = float(input('Entre com o valor de a: '))
#b = float(input('Entre com o valor de b: '))
#c = float(input('Entre com o valor de c: '))
#raizes(a,b,c)

#continua = input('Deseja sair? Digite q ou Enter para novo cálculo:')
#if (continua == 'q'):
#break

#exercicio 3:::::::
#EC= int(input("Qual seu estado civil? digite 1- casado(a), 2- solteiro(a) \n" ))
#sexo= int(input("digite o numero de seu sexo: 1-masculino 2-feminino    \n"))
#if (EC ==1 and sexo==2):
#tempo=int(input("quantos anos você está casado(a)? \n"))
#print(" você está casado(a) há: ", tempo, "anos")
#else:
#print("você está solteiro(a).")

#exercicio 8:::::
#x1=int(input("digite o primeiro numero:  \n"))
#x2=int(input("digite o segundo numero:  \n"))
#x3=int(input("digite o terceiro numero:  \n"))
#x4=int(input("digite o quarto numero:  \n"))
#x5=int(input("digite o quinto numero:  \n"))
#soma=x1+x2+x3+x4+x5
#print("a some dos numeros é: ",soma)
#media=soma/5
#print("a media dos numeros é: ",media)

#exercicio 12::::::
#x=int(input("digite o numero que deseja ver a tabuada. \n"))
#i=0
#while i<10:
#i=i+1
#tab=x*i
#print(x,"X",i, "=",tab)

#x=int(input("digite um numero qualquer: \n"))
#num=x%2
#if num==1:
#result=x+8
#print(result)
#else:
#result=x+5
#print(result)
#x=int(input("digite um numero qualquer: \n"))
#num=x%2
#if num==1:
#print("seu número é impar.")
#else:
#print("seu número é par.")

#EC= int(input("Qual seu estado civil? digite 1- casado(a), 2- solteiro(a) \n" ))
#sexo= int(input("digite o numero de seu sexo: 1-masculino 2-feminino    \n"))
#if (EC ==1 and sexo==2):
#tempo=int(input("quantos anos você está casado(a)? \n"))
# print(" você está casado(a) há: ", tempo, "anos")
#else:
#print("você está solteiro(a).")
#valor=int(input("digite o numero que queira multiplicar por 7\n"))
#tabuada=valor*7
#print("o numero ",valor, "vezes sete é :",tabuada)

#print('Pode digitar seu nome com letras maiúsculas, minúsculas ou mistas.')
#nome = input('Digite seu nome: ').upper()
#invNome = nome[::-1]
#x = list(invNome)
#print(x)
#for i in invNome:
#print(i, end = '\n')
#x = int(input("informe o número que deseja : "))
#if x > 0:
#resultado = x * 2
#print("\n o seu número é positivo e o dobro dele é: ", resultado)
#if x < 0:
#resultado = x * 3
#print("\n o seu número é negativo e o triplo dele é: ",resultado)

#x = int(input("escolha sua operação: \n 1 : Soma \n 2 : Subtração \n 3 : Multiplicação \n 4 : Divisão\nR: "))
#if x==1:
#a = int(input("Informe o primeiro numero da operação: "))
#b = int(input("Informe o segundo numero da operação: "))
#resultado = a + b
#print(a ," + ", b ," = ", resultado)
#if x == 2:
#a = int(input("\n Informe o primeiro numero da operação: "))
#b = int(input("\n Informe o segundo numero da operação: "))
#resultado = a - b
#print(a ," - ", b ," = ", resultado)
#if x== 3:
#a = int(input("Informe o primeiro numero da operação: "))
#b = int(input("Informe o segundo numero da operação: "))
#resultado = a * b
#print(a ," * ", b ," = ", resultado)
#if x== 4:
#if b <=0:
#print("Não tem como dividir um número por Zero")
#a = int(input("Informe o primeiro numero da operação: "))
#b = int(input("Informe o segundo numero da operação: "))
#resultado = a / b
#print(a ," / ", b ," = ", resultado)

#aluno = int(input("Digite sua nota: "))
#if aluno == 10
#print("você está qualificado para o conceito A")
#if aluno >= 8:
#if aluno <= 9:
#print ("você está qualificado para o conceito B")
#if aluno >= 6:
#if aluno <= 7:
#print("você está qualificado para o conceito C")
#if aluno <=5:
#if aluno >=3:
#print("você está qualificado para o conceito D")
#if aluno <3:
#print ("você está qualificado para o conceito E")

#valor = int(input("Digite um valor entre 1 & 9: "))
#if valor > 1:
#if valor < 9:
#print("o valor está na faixa de valor permitida")
#else:
#print("não está na faixa de valor permitida")
#else:
#print("não está na faixa de valor permitida")

# Cálculo do Índice de Massa Corporal

#altura = float(input("Digite sua altura em metros: "))
#peso = float(input("Digite seu peso em Kg: "))

#imc = peso / altura**2

#print("Seu IMC é: %.3f" % imc)

#if imc < 18.5:
#	print ("Abaixo do peso")
#if imc > 18.5:
#  if imc < 25:
#    print("normal")
#if imc > 25:
#  if imc < 30:
#	  print("acima do peso")
#if imc > 30:
#  print("gordo")
