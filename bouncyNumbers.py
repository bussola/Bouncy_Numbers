"""
Autor: Vinicius Magaton Bussola
Data: 26/04/2019

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
for example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number;
for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number;
for example, 155349. Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the
proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the
proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%

"""

# Verifica se numero é crescente
def numCrescente(num):
	num_string = str(num)
	num_anterior = None
	for n in num_string: # Percorre cada algarismo
		if num_anterior: # Pula o primeiro
			if num_anterior > n: # Se o numero da equerda for maior que o da direita, retorna false
				return False
		num_anterior = n # Guarda o numero
	return True


# Verifica se numero é decrescente
def numDecrescente(num):
	num_string = str(num)
	num_anterior = None
	for n in num_string:
		if num_anterior:
			if num_anterior < n: # Se o numero da esquerda for menor que o da direita, retorna false
				return False
		num_anterior = n
	return True


# Verifica se numero é bouncy
def numBouncy(num):
	if not numDecrescente(num) and not numCrescente(num): # Se o numero nao for cres ou decresc, ele é bouncy
		return True
	else:
		return False


def main():
	numero = 99
	bouncy_count = 0
	porcentagem = 0
	while porcentagem != 99:
		numero += 1
		if numBouncy(numero):
			bouncy_count += 1
		porcentagem = (bouncy_count*100.0)/numero
		print (str(numero) + " -> " + str(porcentagem) + "%")
	print("No numero " + str(numero) + ", 99% é bouncy")


#Inicia a função main
if __name__ == '__main__':
    main()