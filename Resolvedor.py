from random import choice
from tqdm import tqdm
from Cubo import Cubo

class IDA_star(object):
    def __init__(self, heuristic, max_depth = 20):
        self.max_depth = max_depth
        self.limite = max_depth
        self.min_limite = None
        self.heuristic = heuristic
        self.moves = []
        
    def run(self, state):
        while True:
            status = self.search(state, 1)
            if status: return self.moves
            self.moves = []
            self.limite = self.min_limite
        return []
    
    def search(self, state, g_score):
        cubo = Cubo(state = state)
        if cubo.resolvido():
            return True
        elif len(self.moves) >= self.limite:
            return False
        min_val = float('inf')
        best_action = None
        for a in [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cubo.n)]:
            cubo = Cubo(state=state)
            if a[0] == 'h':
                cubo.horizontal_twist(a[1], a[2])
            elif a[0] == 'v':
                cubo.vertical_twist(a[1], a[2])
            elif a[0] == 's':
                cubo.side_twist(a[1], a[2])
            if cubo.resolvido():
                self.moves.append(a)
                return True
            cubo_str = cubo.stringfy()
            h_score = self.heuristic[cubo_str] if cubo_str in self.heuristic else self.max_depth
            f_score = g_score + h_score
            if f_score < min_val:
                min_val = f_score
                best_action = [(cubo_str, a)]
            elif f_score == min_val:
                if best_action is None:
                    best_action =[(cubo_str, a)]
                else:
                    best_action.append((cubo_str, a))
        if best_action is not None:
            if self.min_limite is None or min_val < self.min_limite:
                self.min_limite = min_val
            next_action = choice(best_action)
            self.moves.append(next_action[1])
            status = self.search(next_action[0], g_score + min_val)
            if status: return status
        return False
    
    def build_heuristic_db(state, actions, max_moves = 20, heuristic = None):
        if heuristic is None:
            heuristic = {state: 0}
        que = [(state, 0)]
        node_count = sum([len(actions) ** (x + 1) for x in range(max_moves + 1)])
        with tqdm(total=node_count, desc='Heuristic DB') as pbar:
            while True:
                if not que:
                    break
                s, d = que.pop()
                if d > max_moves:
                    continue
                for a in actions:
                    cubo = Cubo(state=s)
                    if a[0] == 'h':
                        cubo.horizontal_twist(a[1], a[2])
                    elif a[0] == 'v':
                        cubo.vertical_twist(a[1], a[2])
                    elif a[0] == 's':
                        cubo.side_twist(a[1], a[2])
                    a_str = cubo.stringfy()
                    if a_str not in heuristic or heuristic[a_str] > d + 1:
                        heuristic[a_str] = d + 1
                    que.append((a_str, d+1))
                    pbar.update(1)
        return heuristic