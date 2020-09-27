'''

Atividade assincrona - 27/09/2020 - UFRRJ - Bacharel Ciência da Computação

Escreva 4 programas para resolver seguintes relações de 
recorrências dadas na aula de hoje: Fibonacci, Hanói, Catalan e Steiner.

A entrada dos programas deve ser um número inteiro positivo n
e a saída deve ser o valor da relação de recorrência referente ao programa
para esse valor de n (Fibonacci(n), Hanoi(n), Catalan(n) ou Steiner(n)).

Aluna: Samara Almendane

'''

# Fibonacci
def fibonacci(n):
	if n >= 0:
		if n == 0:
			result = 0
		elif n == 1:
			result = 1
		else:
			result = fibonacci(n-1) + fibonacci(n-2)
	
	return result

def hanoi(n):
	if n > 0:
		if n == 1:
			result = 1
		else:
			result = 2*(hanoi(n - 1)) + 1

	return result

def catalan(n):
	if n >= 0:
		if n <= 1:
			result = 1
		else:
			result = 0
			for i in range(n):
				result += catalan(i)*catalan(n-i-1)

	return result

def steiner(n):
	if n >= 0:
		if n == 0:
			result = 1
		else:
			result = steiner(n-1)+n

	return result

if __name__ == '__main__':

	print('\nNeste programa temos 4 calculadoras de relação de recorrências.\n')
	print('Sendo elas: Fibonacci, Torre de Hanoi, Catalan e Steiner')
	print('Escolha uma das calculadoras e o número de entrada')

	print(' ')

	caractere = input('Entre com: F para Fibonacci, H para Hanoi, C para Catalan, S para Steiner:\n')
			
	if caractere == 'f' or caractere == 'F':
		num = int(input('\nEntre com um inteiro positivo: '))
		print('Fibonacci = ',fibonacci(num))
	elif caractere == 'h' or caractere == 'H':
		num = int(input('\nEntre com um inteiro positivo: '))
		print('Hanoi = ',hanoi(num))
	elif caractere == 'c' or caractere == 'C':
		num = int(input('\nEntre com um inteiro positivo: '))
		print('Catalan = ', catalan(num))
	elif caractere == 's' or caractere == 'S':
		num = int(input('\nEntre com um inteiro positivo: '))
		print('Steiner = ', steiner(num))
	else:
		print('Valor de entrada errado.')


#print(fibonacci(10))
#print(hanoi(10))
#print(catalan(3))
#print(steiner(5))