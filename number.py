from pip._vendor.distlib.compat import raw_input
import random

people = raw_input("How many gifts are under the tree? ")
print("Generating random numbers for a party of " + people + "... ")
print()

randomlist = []
for i in range(0, 6):
    n = random.randint(1,10)
    if n not in randomlist: randomlist.append(n)
    if people
    
print(randomlist)
""" print(random.choice())
print(n) """


