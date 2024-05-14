from Torre_Hanoi_model import Torre

if __name__=='__main__':
    
    #InitialState
    array_1 = [5,4,3,2,1]
    array_2 = [0,0,0,0,0]
    array_3 = [0,0,0,0,0]

    hanoi = Torre(array_1, array_2, array_3)

    #print('Estado inicial: ', hanoi.initial_state)
    #print('Estado objetivo: ', hanoi.goal_state)
    
    i = 0  #contador de numero de movimientos
    while hanoi.tower_state != hanoi.goal_state:
        i+=1  #Contador de movimientos
        hanoi.find_possible_moves()
        hanoi.forward()
        #hanoi.check_if_solution()
        print('Movimientos: ',i)
        print(hanoi.tower_state)
    