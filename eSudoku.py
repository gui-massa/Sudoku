class Matriz9x9:
    def __init__(self, sudoku):
        """
        :type sudoku: sudoku must be separated by spaces and lines. Exemple:

Errada:
1 3 2 5 7 9 4 6 8
4 9 8 2 6 1 3 7 5
7 5 6 3 8 4 2 1 9
6 4 3 1 5 8 7 9 2
5 2 1 7 9 3 8 4 6
9 8 7 4 2 5 6 3 1
2 1 4 9 3 6 5 8 7
3 6 5 8 1 7 9 2 4
8 7 9 6 4 2 1 5 3

Correta:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9

Desafio:
5 3 4 6 7 8 9 1 0
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
        """
        self._sudoku = sudoku

        self.linha0 = sudoku[0]
        self.linha1 = sudoku[1]
        self.linha2 = sudoku[2]
        self.linha3 = sudoku[3]
        self.linha4 = sudoku[4]
        self.linha5 = sudoku[5]
        self.linha6 = sudoku[6]
        self.linha7 = sudoku[7]
        self.linha8 = sudoku[8]

        self.coluna0 = (sudoku[0][0] + ' ' + sudoku[1][0] + ' ' + sudoku[2][0] + ' ' + sudoku[3][0] + ' ' + sudoku[4][0] + ' ' + sudoku[5][0] + ' ' + sudoku[6][0] + ' ' + sudoku[7][0] + ' ' + sudoku[8][0]).split()
        self.coluna1 = (sudoku[0][1] + ' ' + sudoku[1][1] + ' ' + sudoku[2][1] + ' ' + sudoku[3][1] + ' ' + sudoku[4][1] + ' ' + sudoku[5][1] + ' ' + sudoku[6][1] + ' ' + sudoku[7][1] + ' ' + sudoku[8][1]).split()
        self.coluna2 = (sudoku[0][2] + ' ' + sudoku[1][2] + ' ' + sudoku[2][2] + ' ' + sudoku[3][2] + ' ' + sudoku[4][2] + ' ' + sudoku[5][2] + ' ' + sudoku[6][2] + ' ' + sudoku[7][2] + ' ' + sudoku[8][2]).split()
        self.coluna3 = (sudoku[0][3] + ' ' + sudoku[1][3] + ' ' + sudoku[2][3] + ' ' + sudoku[3][3] + ' ' + sudoku[4][3] + ' ' + sudoku[5][3] + ' ' + sudoku[6][3] + ' ' + sudoku[7][3] + ' ' + sudoku[8][3]).split()
        self.coluna4 = (sudoku[0][4] + ' ' + sudoku[1][4] + ' ' + sudoku[2][4] + ' ' + sudoku[3][4] + ' ' + sudoku[4][4] + ' ' + sudoku[5][4] + ' ' + sudoku[6][4] + ' ' + sudoku[7][4] + ' ' + sudoku[8][4]).split()
        self.coluna5 = (sudoku[0][5] + ' ' + sudoku[1][5] + ' ' + sudoku[2][5] + ' ' + sudoku[3][5] + ' ' + sudoku[4][5] + ' ' + sudoku[5][5] + ' ' + sudoku[6][5] + ' ' + sudoku[7][5] + ' ' + sudoku[8][5]).split()
        self.coluna6 = (sudoku[0][6] + ' ' + sudoku[1][6] + ' ' + sudoku[2][6] + ' ' + sudoku[3][6] + ' ' + sudoku[4][6] + ' ' + sudoku[5][6] + ' ' + sudoku[6][6] + ' ' + sudoku[7][6] + ' ' + sudoku[8][6]).split()
        self.coluna7 = (sudoku[0][7] + ' ' + sudoku[1][7] + ' ' + sudoku[2][7] + ' ' + sudoku[3][7] + ' ' + sudoku[4][7] + ' ' + sudoku[5][7] + ' ' + sudoku[6][7] + ' ' + sudoku[7][7] + ' ' + sudoku[8][7]).split()
        self.coluna8 = (sudoku[0][8] + ' ' + sudoku[1][8] + ' ' + sudoku[2][8] + ' ' + sudoku[3][8] + ' ' + sudoku[4][8] + ' ' + sudoku[5][8] + ' ' + sudoku[6][8] + ' ' + sudoku[7][8] + ' ' + sudoku[8][8]).split()

        self.matrizinha0 = (sudoku[0][0] + ' ' + sudoku[0][1] + ' ' + sudoku[0][2] + ' ' + sudoku[1][0] + ' ' + sudoku[1][1] + ' ' + sudoku[1][2] + ' ' + sudoku[2][0] + ' ' + sudoku[2][1] + ' ' + sudoku[2][2]).split()
        self.matrizinha1 = (sudoku[0][3] + ' ' + sudoku[0][4] + ' ' + sudoku[0][5] + ' ' + sudoku[1][3] + ' ' + sudoku[1][4] + ' ' + sudoku[1][5] + ' ' + sudoku[2][3] + ' ' + sudoku[2][4] + ' ' + sudoku[2][5]).split()
        self.matrizinha2 = (sudoku[0][6] + ' ' + sudoku[0][7] + ' ' + sudoku[0][8] + ' ' + sudoku[1][6] + ' ' + sudoku[1][7] + ' ' + sudoku[1][8] + ' ' + sudoku[2][6] + ' ' + sudoku[2][7] + ' ' + sudoku[2][8]).split()
        self.matrizinha3 = (sudoku[3][0] + ' ' + sudoku[3][1] + ' ' + sudoku[3][2] + ' ' + sudoku[4][0] + ' ' + sudoku[4][1] + ' ' + sudoku[4][2] + ' ' + sudoku[5][0] + ' ' + sudoku[5][1] + ' ' + sudoku[5][2]).split()
        self.matrizinha4 = (sudoku[3][3] + ' ' + sudoku[3][4] + ' ' + sudoku[3][5] + ' ' + sudoku[4][3] + ' ' + sudoku[4][4] + ' ' + sudoku[4][5] + ' ' + sudoku[5][3] + ' ' + sudoku[5][4] + ' ' + sudoku[5][5]).split()
        self.matrizinha5 = (sudoku[3][6] + ' ' + sudoku[3][7] + ' ' + sudoku[3][8] + ' ' + sudoku[4][6] + ' ' + sudoku[4][7] + ' ' + sudoku[4][8] + ' ' + sudoku[5][6] + ' ' + sudoku[5][7] + ' ' + sudoku[5][8]).split()
        self.matrizinha6 = (sudoku[6][0] + ' ' + sudoku[6][1] + ' ' + sudoku[6][2] + ' ' + sudoku[7][0] + ' ' + sudoku[7][1] + ' ' + sudoku[7][2] + ' ' + sudoku[8][0] + ' ' + sudoku[8][1] + ' ' + sudoku[8][2]).split()
        self.matrizinha7 = (sudoku[6][3] + ' ' + sudoku[6][4] + ' ' + sudoku[6][5] + ' ' + sudoku[7][3] + ' ' + sudoku[7][4] + ' ' + sudoku[7][5] + ' ' + sudoku[8][3] + ' ' + sudoku[8][4] + ' ' + sudoku[8][5]).split()
        self.matrizinha8 = (sudoku[6][6] + ' ' + sudoku[6][7] + ' ' + sudoku[6][8] + ' ' + sudoku[7][6] + ' ' + sudoku[7][7] + ' ' + sudoku[7][8] + ' ' + sudoku[8][6] + ' ' + sudoku[8][7] + ' ' + sudoku[8][8]).split()

    @property
    def sudoku(self):
        return self._sudoku

    @sudoku.getter
    def sudoku(self, new_sudoku):
        self._sudoku = new_sudoku

    def e_sudoku(self):
        condicao1 = False  #condição para verificar se foram inseridos todos os 81 números esperados
        condicao2 = False  #condição para verificar se os números estão todos de 1 a 9
        condicao3 = True  #condição para linhas com valores diferentes

        todas_as_listas = [self.linha0, self.linha1, self.linha2, self.linha3, self.linha4, self.linha5, self.linha6, self.linha7, self.linha8,
                           self.coluna0, self.coluna1, self.coluna2, self.coluna3, self.coluna4, self.coluna5, self.coluna6, self.coluna7, self.coluna8,
                           self.matrizinha0, self.matrizinha1, self.matrizinha2, self.matrizinha3, self.matrizinha4, self.matrizinha5, self.matrizinha6, self.matrizinha7, self.matrizinha8]

        lista_com_valores = []
        for lista in todas_as_listas:
            lista_com_valores.extend(lista)

        if len(lista_com_valores) == 243:
            condicao1 = True
        else:
            print('Falha condição 1, faltam valores')

        # print(f'SET: {sorted(set(lista_com_valores))}')
        if sorted(set(lista_com_valores)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            condicao2 = True
        else:
            print('Falha condição 2, insira apenas números de 1 a 9')

        for lista in todas_as_listas:
            if len(lista) != len(set(lista)):
                print(f'Falha condição 3. lista {lista}')
                condicao3 = False

        if condicao1 and condicao2 and condicao3:
            print('\nSolução CORRETA de sudoku. Parabéns!')
        else:
            print('\nSoluação ERRADA. Tente novamente...')


print("\nEscreva abaixo a matriz:")
sudoku1 = []
counter = 0

for linhas in range(9):
    linha = []

    for colunas in range(1):
        entrada = input()
        entrada = entrada.split()
        linha.extend(entrada)

    sudoku1.append(linha)

matriz1 = Matriz9x9(sudoku1)

print(sudoku1)

print('Linhas')
print(matriz1.linha0)
print(matriz1.linha1)
print(matriz1.linha2)
print(matriz1.linha3)
print(matriz1.linha4)
print(matriz1.linha5)
print(matriz1.linha6)
print(matriz1.linha7)
print(matriz1.linha8)

print('Colunas')
print(matriz1.coluna0)
print(matriz1.coluna1)
print(matriz1.coluna2)
print(matriz1.coluna3)
print(matriz1.coluna4)
print(matriz1.coluna5)
print(matriz1.coluna6)
print(matriz1.coluna7)
print(matriz1.coluna8)

print('Matrizinhas')
print(matriz1.matrizinha0)
print(matriz1.matrizinha1)
print(matriz1.matrizinha2)
print(matriz1.matrizinha3)
print(matriz1.matrizinha4)
print(matriz1.matrizinha5)
print(matriz1.matrizinha6)
print(matriz1.matrizinha7)
print(matriz1.matrizinha8)

matriz1.e_sudoku()
