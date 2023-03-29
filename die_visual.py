import pygal
from die import Die

#創建一個D6
die = Die()

#將骰子值出的數字存在list裡面
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#對結果可視化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times. "
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')