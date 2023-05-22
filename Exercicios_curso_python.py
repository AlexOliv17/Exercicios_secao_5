#exercicios seçao 05-condicionais

#exer1:
print("digite dois numeros, o maior deles sera retornado:")
first_number = int(input())
second_number = int(input())

if first_number > second_number:
    print(f'O maior numero digitado foi:{first_number}')
else:
    print(f'O maior numero digitado foi:{second_number}')

#exer2:
print("Forneça um numero qualquer(positivo ou negativo):")
number = int(input())

if number > 0:
    number *= number
    print(f'O numero era positivo, seu valor elevado ao quadrado é:{number}')
else:
    print(f'Numero invalido, tente outra vez!')

#exer3:
print("digite um numero:")
number = float(input())

if number > 0:
    raiz_quadrada_number = number**1/2
    print(f'O numero era positivo, e essa é sua raiz quadrada:{raiz_quadrada_number}')
else:
    number *= number
    print(f'O numero é negativo e seu quadrado é:{number}')

#exer4:
print('Digite um numero qualquer:')
number = int(input())

if number > 0:
    number *= number
    raiz_quadrada_number = number**1/2
    print(f'Seu n° era positivo, entao:\n O quadrado do n° é:{number}\n E a raiz quadrada do n° é:{raiz_quadrada_number}')
else:
    print(f'Numero invalido, tente outro.')

#exer5:
print('Digite um numero:')
number = int(input())

if number%2 == 0:
    print(f"Seu numero é PAR!")
else:
    print(f"Seu numero é ÍMPAR!")

#exer6:
print(f"Digite dois numeros:")
first_number = int(input())
second_number = int(input())
difference_numbers = first_number - second_number

if first_number > second_number:
    print(f"O maior numero dos dois é:{first_number}")
else:
    print(f"O maior numero dos dois é:{second_number}")
print(f"A diferença entre eles é: {abs(difference_numbers)}")

#exer7:
print('Digite dois numeros:')
first_number = int(input())
second_number = int(input())

if first_number > second_number:
    bigger_number = first_number
    print(f"Maior numero:{bigger_number}")

elif second_number> first_number:
    bigger_number = second_number
    print(f"Maior numero:{bigger_number}")

if first_number == second_number:
    print(f"Numeros iguais!")

#exer8:
print('Digite suas notas das duas provas:')
first_note = float(input())
second_note = float(input())

if first_note and second_note > 0 and first_note and second_note < 10:
    media_note = (first_note+second_note)/2
    print(f"Sua média foi: {media_note}")
else:
    print(f"Notas inválidas!")
    exit()

#exer9:
print("Digite seu salario, e sua prestação de emprestimo:")
salario = float(input())
prestaçao_imprestimo = float(input())
vinte_porcento_do_salario = (20*salario)/100

if prestaçao_imprestimo > vinte_porcento_do_salario:
    print(f"Empréstimo nao concedido!")
else:
    print(f"Empréstimo concedido com sucesso!")

#exer10:
print("Digite sua altura e sexo(masculino ou feminino):")
height = float(input())
sex = input()

if sex == 'masculino':
    ideal_weight = (72.7*height)-58
    print(f"Seu peso ideial é:{abs(ideal_weight)}")
elif sex == 'feminino':
    ideal_weight = (62.1*height)-44.7
    print(f"Seu peso ideial é:{abs(ideal_weight)}")
else:
    print(f"Sexo inválido!")
