import random
import math
D={
    'H':(-1,0),
    'B':(1,0),
    'G':(0,-1),
    'D':(0,1)
}
def actions(state,R):
    state-=1
    d = ['H', 'B', 'G', 'D']
    actions = []
    for e in range(len(R[state])):
        if R[state][e] != None:
            actions+=[d[e]]
    return actions
def transition(state,action,maze):
    global D
    new_state_coord = tuple()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == state):
                new_state_coord = (i+D[action][0], j+D[action][1])
    return maze[new_state_coord[0]][new_state_coord[1]]
pGibbs = lambda x,actions:math.exp(x)/sum([math.exp(Q[e]) for e in actions])
def pick_action(actions,Q,state):
    
                  
R = [[None,2,None,None],
     [None,2,None,None],
     [-2,-2,None,2],
     [None,None,-3,3],
     [-3,4,-3,None],
     [2,None,None,None]]
Maze = [[1,None,2],
        [3,4,5],
        [6,None,7]]
Q=[[0 for i in range(4)]for e in range(7)]
S = 1
local_actions = actions(S,R)

R =0
print(actions(4,R))
print(transition(1,'B',Maze))