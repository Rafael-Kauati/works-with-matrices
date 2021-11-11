from maTrix import Matrix



if(__name__ == "__main__"):
    print('\nChoose the number of rows(i) and columms(j) of the matrix : ')
    i = int(input('\ni : '))
    j = int(input('\nj : '))
    m = Matrix(i,j)
    m.set_elements()
    m.get_order()

