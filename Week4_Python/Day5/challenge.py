sequence = 'without,hello,bag,world'
sequence = sequence.split(',')
sequence = sorted(sequence)
sequence1 = ""
for item in sequence:
    sequence1 += item + ','
print(sequence1)