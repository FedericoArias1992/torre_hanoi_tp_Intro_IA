#Script para la torre de hanoi:
'''disk 1: smallest | disk 5: biggest
   tower 1: left  |  tower 2: middle'''
from itertools import permutations
import random

class Torre:
    def __init__(self, array_1, array_2, array_3):
        self.n_torres = 3
        self.n_discos = 5
        self.array_1 = array_1
        self.array_2 = array_2
        self.array_3 = array_3
        '''definimos el estado inicial como una lista de listas'''
        self.initial_state = list([self.array_1, self.array_2, self.array_3])
        '''definimos el estado final como la lista invertida del estado inicial'''
        self.goal_state = list([self.array_3, self.array_2, self.array_1])
        self.tower_state = self.initial_state #Estado actual es estado inicial

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
    def possible_move(self, tower_number_n, tower_number_m):
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
        if self.possible_move(tower_number_n, tower_number_m): #Verfiy if move is possible
            disk_at_top_tower_m = self.find_top_disk_in_tower(tower_number_m) #Precisamos para saber donde ira el disco movido, buscamos el max value de la torre
            position_disk_at_top_tower_m = self.tower_state[tower_number_m].index(disk_at_top_tower_m)
            #print('disk_at_top_tower_m', disk_at_top_tower_m)
            #print('position_disk_at_top_tower_m: ', position_disk_at_top_tower_m)
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

    def find_possible_moves(self):
        print('Estado actual: ', self.tower_state)
        possible_moves_list = [] 
        # Generar permutaciones de todos contra todos tomando de 2 elementos del rango del 0 al 2
        permutaciones_posibles = list(permutations(range(self.n_torres), 2))
        # Iterar sobre todas las combinaciones posibles de mover un disco de una torre a otra
        for elementos in permutaciones_posibles:
            # Llamar a la función possible_move con los argumentos tower_n y tower_m
            if (self.possible_move(elementos[0], elementos[1])):
                possible_moves_list.append(list(elementos))
        self.possible_moves = possible_moves_list
    
    def forward(self):
        '''decidimos avanzar con un possible move'''
        #n_possible_moves = len(self.possible_moves)
        #Tomamos un valor random de la lista:
        random_value = random.choice(self.possible_moves)  #Es una solucion aleatoria, es probable que lo resuelva, pero no es garantia
        #Faltaria hacer una una optimzacion basada en algoritmo
        #print(self.possible_moves)
        try:
            self.move_disk(random_value[0], random_value[1])
        except IndexError as e: 
            return 'Almost got an Error' 
        
    def check_if_solution(self):
        if self.tower_state == self.goal_state:
            return 'You Won!'
        else: return 'Keep trying' 