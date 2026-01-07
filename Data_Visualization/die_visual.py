from die import Die

die = Die()
results = []
for side in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1,die.n_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)