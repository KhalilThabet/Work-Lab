
import random
import math
import numpy as np
import time
Directions={
    'H':(-1,0),
    'B':(1,0),
    'G':(0,-1),
    'D':(0,1)
}

def actions(state, R):
    state-=1
    D = ['H', 'B', 'G', 'D']
    actions = []
    for i in range(len(R[state])):
        if R[state][i] != None:
            actions+=[D[i]]
    # print("Actions: {}".format(actions))
    return actions

def transition(state,action,maze):
    """Returns next state."""
    global Directions
    new_state_coord = tuple()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (maze[i][j] == state):
                new_state_coord = (i+Directions[action][0], j+Directions[action][1])
    # print("From s= {} --> s= {}".format(state, maze[new_state_coord[0]][new_state_coord[1]]))
    return maze[new_state_coord[0]][new_state_coord[1]]

pGibbs = lambda x,actions:math.exp(x)/sum([math.exp(q[e]) for e in actions])

def pick_action(actions, Q, state):
    # picks a random action from actions consedering q matrix.
    # actions c ['H', 'B', 'G', 'D']
    # q = [[0 0 0 0], [0 0 0 0]...]
    # state c {e1, e2, e3} == {1, 2, 3, .., 7}
    D = {
        'H' : 0,
        'B' : 1,
        'G' : 2,
        'D' : 3
    }
    probs = Q[state-1]
    # compute the sum of exp(Q(state, ai))
    probabilities = []
    for action in actions:
        probabilities.append(probs[D[action]])
    probabilities = np.exp(np.array(probabilities))
    
    # GIBBES
    probabilities /= sum(probabilities)
    
    for i in range(1, len(probabilities)):
        probabilities[i] += probabilities[i-1]
    
    probabilities = list(zip(probabilities, actions))
    random_number = random.random()
    chosen_action = None
    # print("Random number= {}".format(random_number))
    for t in probabilities:
        if (random_number < t[0]):
            chosen_action = t[1]
            break
    # print("{} --> {}".format(probabilities, chosen_action))
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
def update_q(q, state, a):
    state-=1
    d = ['H', 'B', 'G', 'D']
    a = d.index(a)
    before_update = q[state][a]
    q[state][a] = (1-ALPHA) * q[state][a] + ALPHA * (R[state][a] + GAMMA * max(q[state]))
    print('Updated q[{}][{}] from {} --> {}'.format(state, a, before_update, q[state][a]))
    for states in range(len(q)):
        for actions in range(len(q[states])):
            if state == states and actions == a:
                print(f"\33[42m"+str(q[states][actions])+f"\033[0m",end=" ")
            else :
                print(q[states][actions],end=" ")
        print()
    print()
        
q=[[0.0 for _ in range(4)] for _ in range(7)]
iteration = 0
for iteration in range(20):
    iteration+=1
    step = 0
    s = 1
    for step in range(200000):
        step +=1
        for i in MAZE:
            for j in i:
                if j==s:
                    print(f"\33[41m"+str(j)+f"\033[0m",end=" ")
                elif (j==None): 
                    print("X",end=" ")
                else :
                    print(j,end=" ")
            print()
        print()
        print("State : {}".format(s))
        acts = actions(s,R)
        act = pick_action(acts, q, s)
        update_q(q, s, act)
        time.sleep(1)
        new_s = transition(s, act, MAZE)
        s = new_s
        if (new_s == 7):
            print("")
            print("HURRAY !!!")
            print("step {}".format(step))
            break
        # print("")
    print("---------iteration {}\n".format(iteration))