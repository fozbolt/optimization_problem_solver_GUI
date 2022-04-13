
"""
Projektni zadatak ...

Autori: Kristijan Krulić, Stjepan Markovčić , Filip Ožbolt
"""

# Import PuLP modeler functions
import pulp
from pulp import *


# Create the 'prob' variable to contain the problem data
prob = LpProblem("Studentski_dom",LpMinimize)


# The 2 variables Beef and Chicken are created with a lower limit of zero
x1=LpVariable("ChickenPercent",0,None,LpInteger)
x2=LpVariable("BeefPercent",0)

