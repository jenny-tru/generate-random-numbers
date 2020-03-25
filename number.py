from pip._vendor.distlib.compat import raw_input
import random

people = raw_input("How many gifts are under the tree? ")
print("Generating random numbers for a party of " + people + "... ")
print()
""" if people is not 'None'
        randomlist.append(n) """

randomlist = []
for i in range(0, int(people)):
    n = random.randint(1,50)
    if n not in randomlist: randomlist.append(n)
   #need to print full amount from input and not repeat values
print(randomlist)


