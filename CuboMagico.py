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
            if direction == 0:#girar a esquerda
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[4][row],
                                                                                              self.cube[1][row])
            elif direction == 1:
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[2][row],
                                                                                              self.cube[3][row])
            else:
                print(f'Error - direction must be 0 (left) or 1 (right)')
                return
            if direction == 0:
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*reversed(self.cube[0]))]
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*reversed(self.cube[5]))] #Transpose bottom
            elif direction == 1: #Twist right
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(*self.cube[0])][::-1] #Transpose top
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(*self.cube[5])][::-1] #Transpose bottom
        else:
            print(f'ERROR - desired row outside of rubiks cube range. Please select a row between 0-{len(self.cube[0])-1}')
            return