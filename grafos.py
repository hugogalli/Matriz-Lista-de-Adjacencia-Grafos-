# TRADUZINDO O CODIGO DO SLIDE PARA A LINGUAGEM PYHTON

# Criando o objeto Grafo que possui numero de verticies e tipo (direcionado ou nao)
class Grafo:
    def __init__(self, qv, dir):
        self.qv = qv
        self.dir = dir


# Utilizando a herança de POO, criei o objeto matriz, que possui os mesmos atributos de um grafo porem é uma matriz
class Matriz(Grafo):
    def __init__(self, qv, dir):
        super().__init__(qv, dir)

        # Inicializando a matriz com 0 em todas as posicoes
        self.matriz = [[0] * self.qv for i in range(self.qv)]

    # Funcao que cria uma aresta na matriz
    def criaAresta(self, u, v):
        self.matriz[u - 1][v - 1] = 1
        if self.dir == 1:
            self.matriz[v - 1][u - 1] = 1

    # Funcao que printa na tela a matriz criada
    def imprimeMatriz(self):
        print("Matriz de adjacência: ")
        for i in range(self.qv):
            print(self.matriz[i])

    # FUNCAO DO EXERCICIO 3 DO SLIDE, VERIFICA OS VERTICES ADJACENTES DE UM VERTICE ESCOLHIDO PELO USUARIO
    # Para a estrutura de matriz
    def chamadasAdjacentes(self, u):
        print(f"Adjacentes de {u}:")
        for i in range(self.qv):
            if self.matriz[u - 1][i] == 1:
                print(f"Vertice: {i + 1}")


# Agora o objeto lista, com a mesma funcao da matriz mas junta no mesmo codigo, herda os atributos de um grafo
class Lista(Grafo):
    def __init__(self, qv, dir):
        super().__init__(qv, dir)

        # Inicializando a lista sem nenhum valor
        self.lista = [[] for i in range(self.qv)]

    # Funcao para criar uma aresta
    def criaAresta(self, u, v, peso):
        self.lista[u - 1].append([v, peso])
        if self.dir == 1 and v != u:
            self.lista[v - 1].append([u, peso])

    # Funcao para printar na tela a lista depois de criada
    def imprimeLista(self):
        print("Lista de adjacencia:")
        for i in range(self.qv):
            print(f"Adjacentes de {i + 1}:")
            for j in self.lista[i]:
                print(f"Vertice: {j[0]}, Peso = {j[1]}")

    # FUNCAO DO EXERCICIO 3 DO SLIDE, VERIFICA OS VERTICES ADJACENTES DE UM VERTICE ESCOLHIDO PELO USUARIO
    # Para a estrutura de lista
    def chamadasAdjacentes(self, u):
        print(f"Adjacentes de {u}:")
        for i in self.lista[u - 1]:
            print(f"Vertice: {i[0]}, Peso = {i[1]}")


# Funcao main do codigo
if __name__ == '__main__':
    escolha = int(input("Escolha entre Lista(1) ou Matriz(2) de adjencia "))

    # Testes para nao termos erros bobos, tal comoo o codigo do slide
    if escolha != 1 and escolha != 2:
        print("Voce inseriu uma escolha invalida, sera utilizada a Lista(1) como padrao.")
        escolha = 1

    # Codigo para LISTAS DE ADJACENCIA
    if escolha == 1:
        while True:
            qv = int(input("Qual a quantidade de vertices do grafo? "))
            if qv <= 0:
                print("Digite um numero positivo valido")
            else:
                break
        dir = int(input("O grafo é Direcionado(1) ou Nao Direcionado(0)? "))
        if dir != 0 and dir != 1:
            print("Voce inseriu uma opcao invalida, sera utilizada a opcao Nao Direcionado(0) ")
            dir = 0

        # Apos realizar todos os testes, obtemos os valores necessarios para construir nosso grafo
        lista = Lista(qv, dir)

        # Loop para ir criando arestas conforme o desejo do usuario
        keep = int(input("Deseja criar uma aresta? Sim(1) Nao(0)"))
        while keep:
            u = int(input("Digite o vertice de origem:"))
            v = int(input("Digite o vertice de destino: "))
            peso = int(input("Digite o peso da aresta: "))
            lista.criaAresta(u, v, peso)
            keep = int(input("Deseja criar outra aresta? Sim(1) Nao(0)"))

    # Codigo para MATRIZES DE ADJACENCIA
    if escolha == 2:
        while True:
            qv = int(input("Qual a quantidade de vertices do grafo? "))
            if qv <= 0:
                print("Digite um numero positivo valido")
            else:
                break
        dir = int(input("O grafo é Direcionado(1) ou Nao Direcionado(0)? "))
        if dir != 0 and dir != 1:
            print("Voce inseriu uma opcao invalida, sera utilizada a opcao Nao Direcionado(0) ")
            dir = 0

        # Apos realizar todos os testes, obtemos os valores necessarios para construir nosso grafo
        matriz = Matriz(qv, dir)

        # Loop para ir criando arestas conforme o desejo do usuario
        keep = int(input("Deseja criar uma aresta? Sim(1) Nao(0)"))
        while keep:
            u = int(input("Digite o vertice de origem:"))
            v = int(input("Digite o vertice de destino: "))
            matriz.criaAresta(u, v)
            keep = int(input("Deseja criar outra aresta? Sim(1) Nao(0)"))

    # Menu para facilitar o uso
    while True:
        print('________________________________________')
        menu = int(input("Printar o grafo criado - 1\n"
                         "Escolher vertice para ver os adjacentes (Ex3) - 2\n"
                         "Sair - 3\n"
                         " "))
        print('________________________________________')
        if menu == 1:
            if escolha == 1:
                lista.imprimeLista()
            else:
                matriz.imprimeMatriz()
        elif menu == 2:
            u = int(input("Escolha o vertice para ver os adjacentes: "))
            if escolha == 1:
                lista.chamadasAdjacentes(u)
            else:
                matriz.chamadasAdjacentes(u)
        elif menu == 3:
            break
