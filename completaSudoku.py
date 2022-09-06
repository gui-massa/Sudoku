def transforma_int(lista):
    """Transforma a lista em int, para podermos somar 1"""
    lista = str(lista)
    lista = str(lista).strip("[]")
    lista = str(lista).replace(', ', '')
    lista = int(lista)
    return lista


def transforma_list(lista_int):
    """Transforma de volta em list, para podermos comparar resultados."""
    lista_list = [int(digito) for digito in str(lista_int)]
    return lista_list


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

A completar:
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 0
1 9 8 3 4 2 5 6 7
8 5 0 7 6 1 4 2 3
4 2 6 8 5 0 7 9 0
7 1 3 9 2 4 8 5 6
9 6 1 0 3 7 2 8 4
2 8 7 4 1 9 6 0 5
3 4 5 2 8 6 1 7 9
        """
        self.sudoku = sudoku


    def e_sudoku(self):
        condicao1 = False  #condição para verificar se foram inseridos todos os 81 números esperados
        condicao2 = False  #condição para verificar se os números estão todos de 1 a 9
        condicao3 = True  #condição para linhas/colunas/matrizinhas com valores diferentes

        self.linha0 = self.sudoku[0]
        self.linha1 = self.sudoku[1]
        self.linha2 = self.sudoku[2]
        self.linha3 = self.sudoku[3]
        self.linha4 = self.sudoku[4]
        self.linha5 = self.sudoku[5]
        self.linha6 = self.sudoku[6]
        self.linha7 = self.sudoku[7]
        self.linha8 = self.sudoku[8]

        self.coluna0 = [self.sudoku[0][0], self.sudoku[1][0], self.sudoku[2][0], self.sudoku[3][0], self.sudoku[4][0], self.sudoku[5][0], self.sudoku[6][0], self.sudoku[7][0], self.sudoku[8][0]]
        self.coluna1 = [self.sudoku[0][1], self.sudoku[1][1], self.sudoku[2][1], self.sudoku[3][1], self.sudoku[4][1], self.sudoku[5][1], self.sudoku[6][1], self.sudoku[7][1], self.sudoku[8][1]]
        self.coluna2 = [self.sudoku[0][2], self.sudoku[1][2], self.sudoku[2][2], self.sudoku[3][2], self.sudoku[4][2], self.sudoku[5][2], self.sudoku[6][2], self.sudoku[7][2], self.sudoku[8][2]]
        self.coluna3 = [self.sudoku[0][3], self.sudoku[1][3], self.sudoku[2][3], self.sudoku[3][3], self.sudoku[4][3], self.sudoku[5][3], self.sudoku[6][3], self.sudoku[7][3], self.sudoku[8][3]]
        self.coluna4 = [self.sudoku[0][4], self.sudoku[1][4], self.sudoku[2][4], self.sudoku[3][4], self.sudoku[4][4], self.sudoku[5][4], self.sudoku[6][4], self.sudoku[7][4], self.sudoku[8][4]]
        self.coluna5 = [self.sudoku[0][5], self.sudoku[1][5], self.sudoku[2][5], self.sudoku[3][5], self.sudoku[4][5], self.sudoku[5][5], self.sudoku[6][5], self.sudoku[7][5], self.sudoku[8][5]]
        self.coluna6 = [self.sudoku[0][6], self.sudoku[1][6], self.sudoku[2][6], self.sudoku[3][6], self.sudoku[4][6], self.sudoku[5][6], self.sudoku[6][6], self.sudoku[7][6], self.sudoku[8][6]]
        self.coluna7 = [self.sudoku[0][7], self.sudoku[1][7], self.sudoku[2][7], self.sudoku[3][7], self.sudoku[4][7], self.sudoku[5][7], self.sudoku[6][7], self.sudoku[7][7], self.sudoku[8][7]]
        self.coluna8 = [self.sudoku[0][8], self.sudoku[1][8], self.sudoku[2][8], self.sudoku[3][8], self.sudoku[4][8], self.sudoku[5][8], self.sudoku[6][8], self.sudoku[7][8], self.sudoku[8][8]]

        self.matrizinha0 = [self.sudoku[0][0], self.sudoku[0][1], self.sudoku[0][2], self.sudoku[1][0], self.sudoku[1][1], self.sudoku[1][2], self.sudoku[2][0], self.sudoku[2][1], self.sudoku[2][2]]
        self.matrizinha1 = [self.sudoku[0][3], self.sudoku[0][4], self.sudoku[0][5], self.sudoku[1][3], self.sudoku[1][4], self.sudoku[1][5], self.sudoku[2][3], self.sudoku[2][4], self.sudoku[2][5]]
        self.matrizinha2 = [self.sudoku[0][6], self.sudoku[0][7], self.sudoku[0][8], self.sudoku[1][6], self.sudoku[1][7], self.sudoku[1][8], self.sudoku[2][6], self.sudoku[2][7], self.sudoku[2][8]]
        self.matrizinha3 = [self.sudoku[3][0], self.sudoku[3][1], self.sudoku[3][2], self.sudoku[4][0], self.sudoku[4][1], self.sudoku[4][2], self.sudoku[5][0], self.sudoku[5][1], self.sudoku[5][2]]
        self.matrizinha4 = [self.sudoku[3][3], self.sudoku[3][4], self.sudoku[3][5], self.sudoku[4][3], self.sudoku[4][4], self.sudoku[4][5], self.sudoku[5][3], self.sudoku[5][4], self.sudoku[5][5]]
        self.matrizinha5 = [self.sudoku[3][6], self.sudoku[3][7], self.sudoku[3][8], self.sudoku[4][6], self.sudoku[4][7], self.sudoku[4][8], self.sudoku[5][6], self.sudoku[5][7], self.sudoku[5][8]]
        self.matrizinha6 = [self.sudoku[6][0], self.sudoku[6][1], self.sudoku[6][2], self.sudoku[7][0], self.sudoku[7][1], self.sudoku[7][2], self.sudoku[8][0], self.sudoku[8][1], self.sudoku[8][2]]
        self.matrizinha7 = [self.sudoku[6][3], self.sudoku[6][4], self.sudoku[6][5], self.sudoku[7][3], self.sudoku[7][4], self.sudoku[7][5], self.sudoku[8][3], self.sudoku[8][4], self.sudoku[8][5]]
        self.matrizinha8 = [self.sudoku[6][6], self.sudoku[6][7], self.sudoku[6][8], self.sudoku[7][6], self.sudoku[7][7], self.sudoku[7][8], self.sudoku[8][6], self.sudoku[8][7], self.sudoku[8][8]]

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

        if sorted(set(lista_com_valores)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            condicao2 = True
        else:
            # print('Falha condição 2, insira apenas números de 1 a 9')
            pass

        for lista in todas_as_listas:
            if len(lista) != len(set(lista)):
                condicao3 = False
                # print(f'Falha condição 3. lista {lista}')

        # print(f'\n {condicao1} {condicao2} {condicao3} ')
        if condicao1 and condicao2 and condicao3:
            print('\nSolução CORRETA de sudoku. Parabéns!')
            return True
        else:
            # print('\nSoluação ERRADA. Tente novamente...')
            return False

    def completa_sudoku(self):
        a_ser_atualizado = []
        for idx1, linha in enumerate(self.sudoku):
            for idx2, numero in enumerate(linha):
                if numero == 0:
                    a_ser_atualizado.append([idx1, idx2])
        print(f'A ser atualizado: {a_ser_atualizado}')

        valores_atualizando = []
        for x in a_ser_atualizado:
            valores_atualizando.append(self.sudoku[x[0]][x[1]])

        for idx, valor in enumerate(valores_atualizando):
            valores_atualizando[idx] = valor + 1
        print(f'valores_atualizando: {valores_atualizando}')

        while True:

            valores_atualizando = transforma_int(valores_atualizando)
            valores_atualizando += 1
            valores_atualizando = transforma_list(valores_atualizando)
            print(f'Valores atualizando: {valores_atualizando}')

            for idx, numero in enumerate(valores_atualizando):
                self.sudoku[a_ser_atualizado[idx][0]][a_ser_atualizado[idx][1]] = numero

            if self.e_sudoku() == True:
                print('\nSudoku completo:\n')
                print(str(self.linha0).strip('[]').replace(',', ''))
                print(str(self.linha1).strip('[]').replace(',', ''))
                print(str(self.linha2).strip('[]').replace(',', ''))
                print(str(self.linha3).strip('[]').replace(',', ''))
                print(str(self.linha4).strip('[]').replace(',', ''))
                print(str(self.linha5).strip('[]').replace(',', ''))
                print(str(self.linha6).strip('[]').replace(',', ''))
                print(str(self.linha7).strip('[]').replace(',', ''))
                print(str(self.linha8).strip('[]').replace(',', ''))
                exit()


# Criando a matriz:
# desta forma estamos criando uma matriz que é basicamente a separação de 9 listas de 9 elementos
# a partir do input do usuário conforme definimos (colunas separada por espaços e linha separada por enter)

print("\nEscreva abaixo a matriz:")
sudoku1 = []
counter = 0

for linhas in range(9):
    linha = []

    for colunas in range(1):
        entrada = input()
        entrada = entrada.split()
        linha.extend(entrada)

    linha = [int(numero) for numero in linha]
    sudoku1.append(linha)

matriz1 = Matriz9x9(sudoku1)

matriz1.e_sudoku()
matriz1.completa_sudoku()
