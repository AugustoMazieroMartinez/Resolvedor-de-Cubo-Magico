class CuboMagico:
    cube = [
                [
                    [0, 0, 0], [0, 0, 1], [0, 0, 2],
                    [0, 1, 0], [0, 1, 1], [0, 1, 2],#topo(branco)
                    [0, 2, 0], [0, 2, 1], [0, 2, 2]
                    ],
                    
                [   [1, 0, 0], [1, 0, 1], [1, 0, 2],
                    [1, 1, 0], [1, 1, 1], [1, 1, 2],#esquerda(laranja)
                    [1, 2, 0], [1, 2, 1], [1, 2, 2]
                    ],
                    
                [   [2, 0, 0], [2, 0, 1], [2, 0, 2],
                    [2, 1, 0], [2, 1, 1], [2, 1, 2],#frente(verde)
                    [2, 2, 0], [2, 2, 1], [2, 2, 2]
                    ],
                    
                [   [3, 0, 0], [3, 0, 1], [3, 0, 2],
                    [3, 1, 0], [3, 1, 1], [3, 1, 2],#direita(vermelho)
                    [3, 2, 0], [3, 2, 1], [3, 2, 2]
                    ],
                    
                [   [4, 0, 0], [4, 0, 1], [4, 0, 2],
                    [4, 1, 0], [4, 1, 1], [4, 1, 2],#costas(azul)
                    [4, 2, 0], [4, 2, 1], [4, 2, 2]
                    ],
                    
                [   [5, 0, 0], [5, 0, 1], [5, 0, 2],
                    [5, 1, 0], [5, 1, 1], [5, 1, 2],#fundo(amarelo)
                    [5, 2, 0], [5, 2, 1], [5, 2, 2]
                    ]
            ]
     
    def horizontal_twist(self, row, direction):
        if row < len(self.cube[0]):
            if direction == 0:#girar a direita
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[4][row],
                                                                                              self.cube[1][row])
            elif direction == 1:#girar a esquerda
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[2][row],
                                                                                              self.cube[3][row])
            else:
                print(f'Error - direction must be 0 (rght) or 1 (left)')
                return
            if direction == 0:#girar direita
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]#transpose top
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))] #Transpose bottom
            elif direction == 1: #girar esquerda
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*self.cube[0])][::-1] #Transpose top
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*self.cube[5])][::-1] #Transpose bottom
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
            if direction == 0:
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*reversed(self.cube[1]))]#transpose left
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(*reversed(self.cube[3]))]#transpose right
            if direction == 0:
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(*self.cube[1])][::-1]#transpose left
                if column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for z in zip(*self.cube[3])][::-1]#transpose right
        else:
            print(f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cube[0]-1)}')
    