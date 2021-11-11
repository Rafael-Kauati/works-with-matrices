import numpy as np
class Matrix:
    def __init__(m, number_rows:int, number_columms:int):
        
        m.i = number_rows - 1
        m.j = number_columms - 1

        m.Mtx : list


    def get_order(m) -> int:
        print(f'A matrix of order : {m.i},{m.j}\n')


    def set_elements(m):

        matrix = m.Mtx = list([])
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
                print(matrixNP)


