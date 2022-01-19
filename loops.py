import random
print("Hello World")

for i in range(1,13):
    print (i)
for j in range(8,41,2):
    print (j)
for k in range(20,-21,-5):
    print(k)
   
ham = input()
for h in range(0,int(ham)):
    print ("hampter")
   
number = 0
for number in range(0,9999):
    number = int(random.randrange(1,31))
    if number == 7:
        print ("7 broek loop")
        break
    print(number)


class Dice:
    def __init__(self, sides):
        self.sides = int(sides)+1
        self.rolls = 0
    def roll(self):
        self.rolls += 1
        return print(random.randrange(1, self.sides))

    def print(self):
        print("This Die has " + str(self.sides-1) + " sides!");
        print("This Die has been rolled " + str(self.rolls) + " times!");
die = Dice(6)
die2 = Dice(20)
while True:
   
    die.roll()
    die.print()
    die2.roll()
    die2.print()
