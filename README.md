# Schelling's Model of segregation

In 1971, the American economist Thomas Schelling created an agent-based model that explain why segregation is so difficult to combat. 
His model showed that even when individuals didn't mind being surrounded or living by agents of a different race, they would still choose to segregate themselves from other agents over time! 


## Model's rules

Suppose there are two types of agents: **1** and **2**. The two populations are initially placed into random locations of a neighborhood represented by a grid.

A satisfied agent is one that is surrounded by at least **t** percent of agents that are like itself. The percentage **t** is called the **tolerance threshold**.
* When an agent is satisfied, he stays in his place.
* When an agent is not satisfied, it can be moved to any vacant location in the grid.

## Commands

To run the execution of the model, use the following command

    python3 schelling.py [t] [ratio]
    
**t** is the tolerance threshold in [0, 100] </br>
**ratio** is the proportion of the first population in comparaison with the second population

## Analysis

In our model, the central cells have 8 neighbors, whereas the corner & the border cells have respectively 3 & 5 neighbors.

The first observation is that each range of the tolerance threshold corresponds to a minumum number of neighbors that are required for the settlement of an agent.

Tolerance threshold range | Accepted number of neighbors
------------------- | ---------------------------
{0}                 | [0, 8]
]0, 12.5]           | [1, 8]
]12.5, 25]          | [2, 8]
]25, 37.5]          | [3, 8]
]37.5, 50]          | [4, 8]
]50, 62.5]          | [5, 8]
]62.5, 75]          | [6, 8]
]75, 87.5]          | [7, 8]
]87.5, 100]         | {8}

### For a ratio of 0.5

* **For a tolerance threshold strictly less greater than 50**, and for a ratio of 0.5, all the agents succeed to quickly settle in a cell in the grid. 
The more the tolerance threshold increase, the more time the agents take to find a suitable cell in the grid. 
That's logical because the more the tolerance threshold increase, the more the agents become "demanding" toward the minimum number of neighbors of the same type.

* **For a tolerance threshold greater than 50**: the agents continue to move endlessly, pursuing a cell in the grid with a relatively high number of neighbors of the same type.

### For a ratio near 0

* The first observation of the previous section is valid in this case.

* The second observation of the previous section is partially true in this case. If the number of agents of a particular type is low (ratio = 0.1), the population of the corresponding types may struggle to settle even with a tolerance threshold in [30, 50] because there is not enough people of their type to satisfy their social needs.

### In general

It's really difficult for a population to settle when the threshold is strictly greater that 50, even if there is second population (ratio = 0).
Part of the cause is because the residents of the corner and the border cells will be constantly moving due to the reduced number of neighbor spots.



