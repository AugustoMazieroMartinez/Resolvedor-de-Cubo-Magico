from random import randint, choice
class Cubo:
    def __init__(self, n = 3, cores = ['w', 'o', 'g', 'r', 'b', 'y'], state = None):
        if state is None: 
            self.n = n
            self.cores = cores
            self.reset()
        else:
            self.n = int(len(state) / 6 ** (.5))
            self.cores = []
            self.cubo = [[[]]]
            for i, s in enumerate(state):
                if s not in self.cores: self.cores.append(s)
                self.cubo[-1][-1].append(s)
                if len(self.cubo[-1][-1]) == self.n and len(self.cubo[-1]) < self.n:
                    self.cubo[-1].append([])
                elif len(self.cubo[-1][-1]) == self.n and len(self.cubo[-1]) == self.n and i < len(state) - 1:
                    self.cubo.append([[]])
                    
                    
    def reset(self):
        self.cubo = [[[c for x in range(self.n)] for y in range(self.n)] for c in self.cores]


    def resolvido(self):
        for lado in self.cubo:
            hold = []
            check = True
            for row in lado:
                if len(set(row)) == 1:
                    hold.append(row[0])
                else:
                    check = False
                    break
            if check == False:
                    break
            if len(set(hold)) > 1:
                    check = False
                    break
        return check
        
        def stringfy(self):
            return ''.join([i for r in self.cubo for s in r for i in s])
        
        
        def embaralhar(self, l_rot = 5, u_rot = 100):
            moves = randint(l_rot, u_rot)
            actions = [
                ('h', 0),
                ('h', 1),
                ('v', 0),
                ('v', 1),
                ('s', 0),
                ('s', 1)
            ]
            
            for i in range(moves):
                a = choice(actions)
                j = randint(0, self.n - 1)
                if a[0] == 'h':
                    self.horizontal_twist(j, a[1])
                elif a[0] == 'v':
                    self.vertical_twist(j, a[1])
                elif a[0] == 's':
                    self.side_twist(j, a[1])
            
            
    def show(self):
        espaco = f'{" " * (len(str(self.cubo[0][0])) + 2)}'
        l1 = '\n'.join(espaco + str(c) for c in self.cubo[0])
        l2 = '\n'.join('  '.join(str(self.cubo[i][j]) for i in range(1,5)) for j in range(len(self.cubo[0])))
        l3 = '\n'.join(espaco + str(c) for c in self.cubo[5])
        print(f'{l1}\n\n{l2}\n\n{l3}')
            
            
    def resolvido(self):
        for lado in self.cubo:
            hold = []
            check = True
            for linha in lado:
                if len(set(linha)) == 1:
                    hold.append(linha[0])
                else:
                    verifica = False
                    break
            if verifica == False:
                break
            if len(set(hold)) > 1:
                verifica = False
                break
        return verifica

    def horizontal_twist(self, row, direction):
        if row < len(self.cube[0]):
            if direction == 0:#girar a esquerda
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[4][row],
                                                                                              self.cube[1][row])
            elif direction == 1:#girar a direita
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[2][row],
                                                                                              self.cube[3][row])
            else:
                print(f'Error - direction must be 0 (rght) or 1 (left)')
                return
            if direction == 0:#girar esquerda
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]#Transpões o topo
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))] #Transpões o fundo
            elif direction == 1: #girardireita
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*self.cube[0])][::-1] #Transpões o topo
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*self.cube[5])][::-1] #Transpões o fundo
        else:
            print(f'ERROR - desired row outside of rubiks cube range. Please select a row between 0-{len(self.cube[0])-1}')
            return
    def vertical_twist(self, column, direction):
        if column < len(self.cube):
            if direction == 1: #girar para baixo
                self.cube[0][column], self.cube[2][column], self.cube[4][column], self.cube[5][column] = (self.cube[2][column],
                                                                                                          self.cube[4][column],
                                                                                                          self.cube[5][column],
                                                                                                          self.cube[0][column])
            elif direction == 0:
                self.cube[0][column], self.cube[2][column], self.cube[4][column], self.cube[5][column] = (self.cube[5][column],
                                                                                                          self.cube[0][column],
                                                                                                          self.cube[2][column],
                                                                                                          self.cube[4][column])
            else:
                print('Error - direction must be 0(up) or 1(down)')
            if direction == 0: #gira para baixo
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))][::-1]#Transpõe para esquerda
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))][::-1]#Transpõe para direita
            if direction == 1: #gira para cima
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*self.cube[1])]#Transpõe para esquerda
                if column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*self.cube[3])]#Transpõe para direita
        else:
            print(f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cube[0]-1)}')
    def side_twist(self, row, direction):
        if row < len(self.cube):
            if direction == 1:#girar direita
                self.cube[0][row], self.cube[3][row], self.cube[5][row], self.cube[1][row] = (self.cube[3][row],
                                                                                              self.cube[5][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[0][row])
            elif direction == 0:#girar esquerda
                self.cube[1][row], self.cube[5][row], self.cube[3][row], self.cube[0][row] = (self.cube[5][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[0][row],
                                                                                              self.cube[1][row])
            else:
                print('Error - direction must be 0(right) or 1(left)')
            if direction == 0:#girar direita
                if row == 0:
                    self.cube[4] = [list(x) for x in zip(*reversed(self.cube[4]))]#Transpõe para frente
                elif row == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(*reversed(self.cube[2]))] #Transpõe para trás
            elif direction == 1: #girar esquerda
                if row == 0:
                    self.cube[4] = [list(x) for x in zip(*self.cube[4])][::-1] #Transpõe para frente
                elif row == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(*self.cube[2])][::-1] #Transpõe para trás
        else:
            print(f'ERROR - desired row outside of rubiks cube range. Please select a row between 0-{len(self.cube[0] - 1)}')