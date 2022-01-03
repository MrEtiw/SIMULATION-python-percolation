# Simulation of Percolating Systems, using Python

**CONTEXT**: 

Personal project, intended to replicate and improve thrid year physics engineering capstone project. See: LINK

**DESCRIPTION**:
- Intends to simulate percolating systems.
- Given a probability for each element of a specific lattice, what is the probability that there exists a percolating path through the system?
- Explanations and comments written in English.

**LANGUAGES / TECH**:
- Python
- Numpy library
- Matplotlib library

**ADDITIONAL INFOS:**












Percolation refers to the movement and filtering of fluids though porous materials.
Therefore, it refers to the movement of particules through a lattice.
This project simulates a "system" with a lattice (grid).
Each point of the grid can be "filled" (1) or "empty" (0).
A "percolation path" is a continuous path of filled points across the system (from left to right).
This could represent water flowing through coffee grinds, an electric current follwowing conductive islands, etc.


## A long time ago
I simulated percolating systems in matlab as a physics students.
I now want to give it a try in Python, with a bit more structure.

## What's a percolating system?
A percolating system is defined by a lattice, meaning a repeating arrangement of points.
Each point has a form that defines its neighbors.


## What can we study with percolating systems?
- If each point has a probability p of being "filled", for a given lattice topology, what is the probability that the system is percolating (meaning that there exists a continuous path across the lattice).
- How can we establish if there is a percolating path in a system?
- How does changing the lattice toopology affects all of this?
- What if there is obstacles that prohibite percolation?


