
import random
import math
import numpy as np
D={
    'H':(-1,0),
    'B':(1,0),
    'G':(0,-1),
    'D':(0,1)
}

def actions(state, r):
    state-=1
    d = ['H', 'B', 'G', 'D']
    actions = []
    # print("R[state]= ", r[state])
    for i in range(len(r[state])):
        if r[state][i] != None:
            actions+=[d[i]]
    print("Actions: {}".format(actions))
    return actions

def transition(state,action,maze):
    """Returns next state."""
    global D
    new_state_coord = tuple()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == state):
                new_state_coord = (i+D[action][0], j+D[action][1])
    print("From s= {} --> s= {}".format(state, maze[new_state_coord[0]][new_state_coord[1]]))
    return maze[new_state_coord[0]][new_state_coord[1]]

pGibbs = lambda x,actions:math.exp(x)/sum([math.exp(q[e]) for e in actions])

def pick_action(actions, q, state):
    # picks a random action from actions consedering q matrix.
    # actions c ['H', 'B', 'G', 'D']
    # q = [[0 0 0 0], [0 0 0 0]...]
    # state c {e1, e2, e3} == {1, 2, 3, .., 7}
    d = {
        'H' : 0,
        'B' : 1,
        'G' : 2,
        'D' : 3
    }
    probs = q[state]
    # compute the sum of exp(Q(state, ai))
    probabilities = []
    for action in actions:
        probabilities.append(probs[d[action]])
        # print("PROB[d[action]]= {}".format(probs[d[action]]))
    
    # GIBBES
    probabilities = np.exp(np.array(probabilities)) / sum(np.exp(np.array(probabilities)))
    
    for i in range(1, len(probabilities)):
        probabilities[i] += probabilities[i-1]
    
    probabilities = list(zip(probabilities, actions))
    random_number = random.random()
    chosen_action = None
    print("Random number= {}".format(random_number))
    for t in probabilities:
        if (random_number < t[0]):
            chosen_action = t[1]
            break
    print("{} --> {}".format(probabilities, chosen_action))
    if (chosen_action == None):
        print("YOO CHECK pick_action FUNCTION.")
        exit(-1)
    return chosen_action


R = [[None,2,None,None],
     [None,2,None,None],
     [-2,-2,None,2],
     [None,None,-3,3],
     [-3,4,-3,None],
     [2,None,None,None]]
MAZE = [[1,None,2],
        [3,4,5],
        [6,None,7]]
ALPHA = 0.5
GAMMA = 0.5
REWARD = 2

q=[[0 for _ in range(4)] for _ in range(7)]

s = 1
for _ in range(2):
    print("State : {}".format(s))
    acts = actions(s,R)
    act = pick_action(acts, q, s)
    
    new_s = transition(s, act, MAZE)
    s = new_s
    print("")
# update Q;


# print(actions(4,R))
# print(transition(1,'B',MAZE))
# print(pick_action(actions(4,R), q, 4))