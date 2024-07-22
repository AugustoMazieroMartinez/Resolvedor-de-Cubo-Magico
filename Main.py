import json
import os.path

from Cubo import Cubo
from Resolvedor import IDA_star, build_heuristic_db

MAX_MOVES = 20
NEW_HEURISTICS = False
HEURISTIC_FILE = 'heuristic.json'

cubo = Cubo(n=3)
cubo.show()
print('-------------')
#--------------------------------------------

if os.path.exists(HEURISTIC_FILE):
    with open(HEURISTIC_FILE) as f:
        h_db = json.load(f)
else:
    h_db = None
    
if h_db is None or NEW_HEURISTICS is True:
    actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cubo.n)]
    h_db = build_heuristic_db(
        cubo.stringfy(),
        actions,
        max_moves = MAX_MOVES,
        heuristic = h_db
    )
    
    with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            h_db,
            f,
            ensure_ascii=False,
            indent=4
        )
#---------------------------------------------------
        
cubo.embaralhar(
    l_rot= MAX_MOVES if MAX_MOVES < 5 else 5,
    u_rot= MAX_MOVES
)

cubo.show()
print('-------------')

solver = IDA_star(h_db)
moves = solver.run(cubo.stringfy())
print(moves)

for m in moves:
    if m[0] == 'h':
        cubo.horizontal_twist(m[1], m[2])
    elif m[0] == 'v':
        cubo.vertical_twist(m[1], m[2])
    elif m[0] == 's':
        cubo.side_twist(m[1], m[2])
        
cubo.show()
