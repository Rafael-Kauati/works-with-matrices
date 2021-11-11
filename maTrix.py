import numpy as np
class Matrix:
    def __init__(m, number_rows:int, number_columms:int):
        
        m.i = number_rows
        m.j = number_columms

        m.Mtx : list

        
        

    def get_order(m) -> int:
        print(f'{m.i},{m.j}')


    def set_elements(m):
        matrix = m.Mtx = list([])
        print(f"______\nInhert the matrix of {m.i}{m.j}")

        for x in range(0, m.i + 1):
            
            matrix.append([])

            for y in range(0, m.j + 1):
                print(f"Inhert the value of the element {x}{y}")

                element_input = input('\n')
                matrix[x].append(element_input)

                if(y == m.j):
                    break

            if(x == m.i):
                print(f"\n{m.i}{m.j}\n")
                matrixNP = np.array(matrix)
                print(matrixNP)


