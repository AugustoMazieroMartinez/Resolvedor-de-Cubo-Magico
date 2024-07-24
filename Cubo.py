from random import randint, choice
class CuboMagico:
    def __init__(self, n=3, cores=['w', 'o', 'g', 'r', 'b', 'y'], state=None):
        if state is None:
            self.n = n
            self.cores = cores
            self.reset()
        else:
            self.n = int(len(state) ** 0.5 / 6 ** 0.5)
            self.cores = []
            self.cubo = [[[]]]
            for i, s in enumerate(state):
                if s not in self.cores:
                    self.cores.append(s)
                self.cubo[-1][-1].append(s)
                if len(self.cubo[-1][-1]) == self.n and len(self.cubo[-1]) < self.n:
                    self.cubo[-1].append([])
                elif len(self.cubo[-1][-1]) == self.n and len(self.cubo[-1]) == self.n and i < len(state) - 1:
                    self.cubo.append([[]])
            self._verificar_integridade()
                    
    def _verificar_integridade(self):
        if len(self.cubo) != 6:
            raise ValueError(f"O cubo deveria ter 6 faces, mas tem {len(self.cubo)} faces.")
        for face in self.cubo:
            if len(face) != self.n or any(len(row) != self.n for row in face):
                raise ValueError("Cada face do cubo deve ser NxN.")
                    
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
        if row < len(self.cubo[0]):
            if direction == 0: #Twist left
                self.cubo[1][row], self.cubo[2][row], self.cubo[3][row], self.cubo[4][row] = (self.cubo[2][row],
                                                                                              self.cubo[3][row],
                                                                                              self.cubo[4][row],
                                                                                              self.cubo[1][row])

            elif direction == 1: #Twist right
                self.cubo[1][row], self.cubo[2][row], self.cubo[3][row], self.cubo[4][row] = (self.cubo[4][row],
                                                                                              self.cubo[1][row],
                                                                                              self.cubo[2][row],
                                                                                              self.cubo[3][row])
            else:
                print('ERRO - Direção deve ser 0(esquerda) ou 1(direita)')
                return
            #Rotating connected face
            if direction == 0: #Twist left
                if row == 0:
                    self.cubo[0] = [list(x) for x in zip(*reversed(self.cubo[0]))] #Transpose top
                elif row == len(self.cubo[0]) - 1:
                    self.cubo[5] = [list(x) for x in zip(*reversed(self.cubo[5]))] #Transpose bottom
            elif direction == 1: #Twist right
                if row == 0:
                    self.cubo[0] = [list(x) for x in zip(*self.cubo[0])][::-1] #Transpose top
                elif row == len(self.cubo[0]) - 1:
                    self.cubo[5] = [list(x) for x in zip(*self.cubo[5])][::-1] #Transpose bottom
        else:
            print(f'ERRO - A coluna selecionada está fora do alcance do cubo. Por favor escolha uma coluna entre 0-{len(self.cubo[0])-1}')
            return

    def vertical_twist(self, column, direction):
        if column < len(self.cubo[0]):
            for i in range(len(self.cubo[0])):
                if direction == 0:
                    self.cubo[0][i][column], self.cubo[2][i][column], self.cubo[4][-i-1][-column-1], self.cubo[5][i][column] = (self.cubo[4][-i-1][-column-1],
                                                                                                                                self.cubo[0][i][column],
                                                                                                                                self.cubo[5][i][column],
                                                                                                                                self.cubo[2][i][column])
                elif direction == 1:
                    self.cubo[0][i][column], self.cubo[2][i][column], self.cubo[4][-i-1][-column-1], self.cubo[5][i][column] = (self.cubo[2][i][column],
                                                                                                                                self.cubo[5][i][column],
                                                                                                                                self.cubo[0][i][column],
                                                                                                                                self.cubo[4][-i-1][-column-1])
                else:
                    print('ERRO - Direção deve ser 0(cima) ou 1(baixo)')
                    return
            #Rotating connected face
            if direction == 0:
                if column == 0:
                    self.cubo[1] = [list(x) for x in zip(*self.cubo[1])][::-1] #Transpose left
                elif column == len(self.cubo[0]) - 1:
                    self.cubo[3] = [list(x) for x in zip(*self.cubo[3])][::-1] #Transpose right
            elif direction == 1:
                if column == 0:
                    self.cubo[1] = [list(x) for x in zip(*reversed(self.cubo[1]))] #Transpose left
                elif column == len(self.cubo[0]) - 1:
                    self.cubo[3] = [list(x) for x in zip(*reversed(self.cubo[3]))] #Transpose right
        else:
            print(f'ERRO - A linha selecionada está fora do alcance do cubo. Por favor escolha uma linha entre 0-{len(self.cubo[0])-1}')
            return
                      
    def side_twist(self, column, direction):
        if column < len(self.cubo[0]):
            for i in range(len(self.cubo[0])):
                if direction == 0:
                    self.cubo[0][column][i], self.cubo[1][-i-1][column], self.cubo[3][i][-column-1], self.cubo[5][-column-1][-1-i] = (self.cubo[3][i][-column-1],
                                                                                                                                      self.cubo[0][column][i],
                                                                                                                                      self.cubo[5][-column-1][-1-i],
                                                                                                                                      self.cubo[1][-i-1][column])
                elif direction == 1:
                    self.cubo[0][column][i], self.cubo[1][-i-1][column], self.cubo[3][i][-column-1], self.cubo[5][-column-1][-1-i] = (self.cubo[1][-i-1][column],
                                                                                                                                      self.cubo[5][-column-1][-1-i],
                                                                                                                                      self.cubo[0][column][i],
                                                                                                                                      self.cubo[3][i][-column-1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            if direction == 0:
                if column == 0:
                    self.cubo[4] = [list(x) for x in zip(*reversed(self.cubo[4]))] #Transpose back
                elif column == len(self.cubo[0]) - 1:
                    self.cubo[2] = [list(x) for x in zip(*reversed(self.cubo[2]))] #Transpose top
            elif direction == 1:
                if column == 0:
                    self.cubo[4] = [list(x) for x in zip(*self.cubo[4])][::-1] #Transpose back
                elif column == len(self.cubo[0]) - 1:
                    self.cubo[2] = [list(x) for x in zip(*self.cubo[2])][::-1] #Transpose top
        else:
            print(f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cubo[0])-1}')
            return