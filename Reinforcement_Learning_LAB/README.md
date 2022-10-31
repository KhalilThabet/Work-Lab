This is a simple 3x3 grid path finder using reinforcement learning.

### Grid

| 1  | X | 2  |
--- | --- | --- 
| 3  | 4 | 5  |
--- | --- | ---
| 6  | X | 7  |


### Description
The agent starts at each iteration from the state 1 and then move forward in the grid following our Reward Matrix for each action to do at each Step. The agent generates as a result his own Q Matrix to keep track of the environment.
<img src="Training.gif">