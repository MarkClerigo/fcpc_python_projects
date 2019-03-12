listChords = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

input_chords = input('Input chords: ')
input_step = int(input('Input step: '))

user_chords = [word for word in input_chords.split()]
print(user_chords)

new = ''
for chord in user_chords:
    if chord in listChords:
        index = listChords.index(chord)
        if index + input_step >= len(listChords):
            x = (index + input_step) - len(listChords)
            new += listChords[x]

        else:
            new += listChords[index+input_step]

print(new)
