import math
import numpy as np
import this
class Matrix:
    def __init__(m, number_rows:int, number_columms:int):
        
        m.i = number_rows
        m.j = number_columms
        

    def get_order(m) -> int:
        print(f'{m.i},{m.j}')


    def set_elements(m):
        print(f"______\nInhert the matrix of {m.i}{m.j}")

        for x in range(0, m.i + 1):
            for y in range(0, m.j + 1):
                print(f"Inhert the value of the element {x}{y}")
                
                if(y == m.j):
                    break

            if(x == m.i):
                print(f"{m.i}{m.j}")



        