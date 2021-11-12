import numpy as np
class Matrix:
    def __init__(m, number_rows:int, number_columms:int):
        
        m.i = number_rows 
        m.j = number_columms 

        matrix = list([])
        print(f'\n_____________\nInsert the value of the each element of the {m.i}{m.j} matrix')

        for x in range(0, m.i + 1):
            
            matrix.append([])

            for y in range(0, m.j + 1):

                element_input = input(f"\n{x}{y} : ")
                matrix[x].append(element_input)

                if(y == m.j):
                    break

            if(x == m.i):
                print(f"\n{m.i}{m.j}\n")
                matrixNP = np.array(matrix)
                m.matrix = matrixNP
                print(matrixNP)



    def get_order(m) -> int:
        print(f'A matrix of order : {m.i},{m.j}\n')
        return {m.i},{m.j}



    def get_element(m):
        print(f'\n_____________Wich element from the {m.i}{m.j} matrix ?')

        number_of_row = int(input('\nRow(i) : '))
        number_of_coluum = int(input('\nColuum(j) : '))
        print('\n',m.matrix[number_of_row, number_of_coluum])