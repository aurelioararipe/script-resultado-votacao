import operator

def ResultadoPorEleitor(candidatos, peso, VPE, qtdEleitoresAptos):
	c = 0
	r = candidatos*[0]
	
	while c < candidatos:
		r[c] = (peso*VPE[c])/qtdEleitoresAptos
		c += 1
	return r
	
def Resultado(resultGeral, categoriaEleitores, candidatos):
	cEleit = 0
	cCand = 0
	resultadoFinal = candidatos*[0]
	
	while cCand < candidatos:
		while cEleit < categoriaEleitores:
			resultadoFinal[cCand] += resultGeral[cEleit][cCand]
			cEleit += 1
		cEleit = 0
		cCand += 1
	return resultadoFinal
	
def main ():
	try:
		#ELEITORES
		categoriaEleitores = int(input('Quantas categorias de eleitores existem? '))
		while categoriaEleitores < 0:
			print("Valor inválido. Insira um valor maior que zero")
			categoriaEleitores = int(input('Quantas categorias de eleitores existem? '))
		nomeCategorias = categoriaEleitores*[0]
		for contCategoriaEleitores in range(categoriaEleitores):
			nomeCategorias[contCategoriaEleitores] = input('Qual nome da categoria '+str(contCategoriaEleitores+1)+'? ')
		print(nomeCategorias)
		print("\n")
		
		contCategoriaEleitores = 0
		validaPeso = 0
		pesos = categoriaEleitores*[0]
		qtdEleitores = categoriaEleitores*[0]
		ganhador = 0
		ganhadorPercentual = 0
		
		while contCategoriaEleitores < categoriaEleitores:
			pesos[contCategoriaEleitores] = int(input('Qual peso do eleitor da categoria '+nomeCategorias[contCategoriaEleitores]+'? '))
			while pesos[contCategoriaEleitores] < 0:
				print("Valor inválido. Insira um valor maior que zero")
				pesos[contCategoriaEleitores] = int(input('Qual peso do eleitor da categoria '+nomeCategorias[contCategoriaEleitores]+'? '))
			validaPeso += pesos[contCategoriaEleitores]
			if validaPeso > 100:
				print("A soma do peso dos votos de todos eleitores nao pode ultrapassar 100. Repita o peso e a quantidade de eleitores aptos a votar")
				contCategoriaEleitores = 0
				validaPeso = 0
			else:
				qtdEleitores[contCategoriaEleitores] = int(input('Qual a quantidade de eleitores da categoria '+nomeCategorias[contCategoriaEleitores]+' aptos a votar? '))
				contCategoriaEleitores += 1
		
		print("\n")
		#CANDIDATOS
		candidatos = int(input('Quantos candidatos existem? '))
		while candidatos < 0:
			print("Valor inválido. Insira um valor maior que zero")
			candidatos = int(input('Quantos candidatos existem? '))	
		nomeCandidatos = candidatos*[0]
		for nCandidato in range(candidatos):
			nomeCandidatos[nCandidato] = input('Qual nome do candidato '+str(nCandidato+1)+'? ')
		print(nomeCandidatos)
		
		print("\n")
		#RESULTADOS
		contCandidatos = 0
		x = 0
		y = 0
		votosRecebidos = [[0 for y in range(candidatos)] for x in range(categoriaEleitores)]
		#VPE votos por eleitor - guarda os votos de uma categoria de eleitor para todos os candidatos
		VPE = candidatos*[0]
		resultGeral = [[0 for y in range(candidatos)] for x in range(categoriaEleitores)]
		resultadoFinal = candidatos*[0]
		contEleitores = 0
		#RPE Resultado por eleitor - recebe o vetor da funcao ResultadoPorEleitor()
		RPE = candidatos*[0]
		rcandidato = 0
		votosRecebidosXAptosVotar = 0
		
		while contEleitores < categoriaEleitores:
			while contCandidatos < candidatos:
				votosRecebidos[contEleitores][contCandidatos] = int(input('Quantos votos o candidato '+nomeCandidatos[contCandidatos]+' recebeu do eleitor de categoria '+nomeCategorias[contEleitores]+'? '))
				while votosRecebidos[contEleitores][contCandidatos] < 0:
					print("Valor inválido. Insira um valor maior que zero")
					votosRecebidos[contEleitores][contCandidatos] = int(input('Quantos votos o candidato '+nomeCandidatos[contCandidatos]+' recebeu do eleitor de categoria '+nomeCategorias[contEleitores]+'? '))
				print(votosRecebidos)
				votosRecebidosXAptosVotar += votosRecebidos[contEleitores][contCandidatos]
				if votosRecebidosXAptosVotar > qtdEleitores[contEleitores]:
					print("A quantidade de votos recebidos desta categoria de eleitor não pode ultrapassar a quantidade de aptos a votar. Repita os votos.")
					contCandidatos = 0
					votosRecebidosXAptosVotar = 0
				else:
					VPE[contCandidatos] = votosRecebidos[contEleitores][contCandidatos]
					contCandidatos += 1
			print("\n")
			votosRecebidosXAptosVotar = 0
			#categoriaEleitores é inteiro; pesos é vetor com tamanho igual a categoria de eleitores; VPE é vetor com tamanho igual ao numero de candidatos, qtdEleitores é vetor com tamanho igual a categoria de eleitores
			RPE = ResultadoPorEleitor(candidatos, pesos[contEleitores], VPE, qtdEleitores[contEleitores])
			while rcandidato < contCandidatos:
				resultGeral[contEleitores][rcandidato] = RPE[rcandidato]
				rcandidato += 1
			rcandidato = 0
			contCandidatos = 0
			contEleitores += 1
		
		print("\n")	
		print("Matriz do resultado geral: ")
		print(resultGeral)
		resultadoFinal = Resultado(resultGeral, categoriaEleitores, candidatos)
		print("Resultado final Main: ")
		for res in range(candidatos):
			print("Candidato "+nomeCandidatos[res]+": "+str(resultadoFinal[res]))
		
		ganhador, ganhadorPercentual = max(enumerate(resultadoFinal, 0), key=operator.itemgetter(1))
		print("Ganhador: "+nomeCandidatos[ganhador])
		print("Percentual de votos de "+nomeCandidatos[ganhador]+": "+str(ganhadorPercentual))
		print("\n")	
		input("Pressione <enter> para fechar o programa")
	except ValueError:
		print("Entrada inválida. Execute o programa novamente e insira informações válidas.")
		input("Pressione <enter> para fechar o programa")
main()