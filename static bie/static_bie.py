import pygal
from random import randint
class Die():


 def __init__(self, num_sides=6):
 
  self.num_sides = num_sides

 def roll(self):
 
	 return randint(1, self.num_sides)

t = 1000
die_1 = Die(8)
die_2 = Die(8)
die_3 = Die(8)
results = []
for i in range(t) :
   sums = die_1.roll() + die_2.roll() + die_3.roll()
   results.append(sums)

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value)  for value in range( 3 , max_result+1)]

hist = pygal.Bar()
hist.title = f"Results of rolling a D8 a D8  and a D8 {t} times."
hist.x_labels = [str(x) for x in range(3, max_result+1)]  
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8 + D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')

