#Script para la torre de hanoi:
'''disk 1: smallest | disk 5: biggest
   tower 1: left  |  tower 2: middle'''
class Torre:
    def __init__(self):
        self.n_torres = 3
        self.n_discos = 5
    def initial_state(self, array_1, array_2, array_3):
        '''definimos el estado inicial como una lista de listas'''
        self.tower_state = list([array_1, array_2, array_3])
    def find_bottom_disk_in_tower(self, tower_number):
        '''verificamos que tamanho de disco tiene la torre tower_number: int'''
        return max(self.tower_state[tower_number])
    def find_top_disk_in_tower(self, tower_number):
        try:
            #Necesitamos el valor del disco mas pequenho excluyendo el 0, ya que si encuentra la funcion encuentra al 0
            #No mueve el disco mas pequenho sino el cero
            min_disk_value_tower = min(filter(lambda x: x > 0, self.tower_state[tower_number]))
        except ValueError as e:
            min_disk_value_tower=0  #caso en que la torre esta vacia
        return min_disk_value_tower
    def posible_move(self, tower_number_n, tower_number_m):
        '''verifies if last disk in tower_n can be moved to tower_m'''
        if self.find_top_disk_in_tower(tower_number_m) == 0:
            '''means the tower is empty'''
            return True #'Possible move!'
        elif self.find_top_disk_in_tower(tower_number_n) < self.find_top_disk_in_tower(tower_number_m):
            #Debe ser estricto mayor pq no existen 2 discos de tamanho igual
            return True #'Possible move!'
        else:
            return False #'Not possible mate, keep trying'
    def move_disk(self, tower_number_n, tower_number_m):
        '''take a the disk at the top of tower n to top of tower m'''
        if self.posible_move(tower_number_n, tower_number_m): #Verfiy if move is possible
            disk_at_top_tower_m = self.find_top_disk_in_tower(tower_number_m) #Precisamos para saber donde ira el disco movido, buscamos el max value de la torre
            position_disk_at_top_tower_m = self.tower_state[tower_number_m].index(disk_at_top_tower_m)
            print('disk_at_top_tower_m', disk_at_top_tower_m)
            print('position_disk_at_top_tower_m: ', position_disk_at_top_tower_m)
            self.tower_state[tower_number_m][position_disk_at_top_tower_m+1]= self.find_top_disk_in_tower(tower_number_n) #add the disk at the top of the tower_n to the tower_m and place it on the bottom of tower_m
            self.tower_state[tower_number_n].remove(self.find_top_disk_in_tower(tower_number_n)) #Borramos el elemento que movimos de la torre_m
            self.tower_state[tower_number_n].append(0)  #Agregamos un nuevo elemento al top de la torre a la cual le sacamos el disco, tal que el array tenga 5 elementos
            try:
                self.tower_state[tower_number_m].append(0) #Esto hay que hacerlo porque si, sino nunca se posiciona al final del array
                self.tower_state[tower_number_m].remove(0) #Esto hay que hacerlo porque si
            except ValueError as e:
                pass
            return self.tower_state
        else: return 'The move is not possible, please check the move first, using posible_move() method'

    
hanoi = Torre()

array_1 = [5,4,3,2,1]
array_2 = [0,0,0,0,0]
array_3 = [0,0,0,0,0]


hanoi.initial_state(array_1, array_2, array_3)

hanoi.find_bottom_disk_in_tower(0)
hanoi.find_top_disk_in_tower(0)

print(hanoi.posible_move(0,1))
print(hanoi.posible_move(1,2))
print(hanoi.posible_move(0,2))
print(hanoi.move_disk(0,1))
print(hanoi.move_disk(0,2))
print(hanoi.move_disk(1,2))
print(hanoi.move_disk(2,0))
print(hanoi.move_disk(0,1))
print(hanoi.move_disk(0,2))
