import math

n = int(input())
notes = []
dNotes = set()
d = {
    "G": 10, "A": 0, "B": 2, "C": 3, "D": 5, "E": 7, "F#": 9, "A#": 1, "Bb": 1, "C#": 4, "Db": 4, "D#": 6,
    "Eb": 6, "Gb": 9, "F": 8, "G#": 11, "Ab": 11
}
keys = {
    "G major":
        ["G", "A", "B", "C", "D", "E", "F#"],
    "C major": ["C", "D", "E", "F", "G", "A", "B"],
    "Eb major": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "F# minor": ["F#", "G#", "A", "B", "C#", "D", "E"],
    "G minor": ["G", "A", "Bb", "C", "D", "Eb", "F"]
}
keysNum = {
    "G major": [d[k] for k in keys["G major"]],
    "C major": [d[k] for k in keys["C major"]],
    "Eb major": [d[k] for k in keys["Eb major"]],
    "F# minor": [d[k] for k in keys["F# minor"]],
    "G minor": [d[k] for k in keys["G minor"]]
}

for i in range(n):
    no = round(12 * math.log(float(input()) / 440, 2)) % 12
    notes.append(no)
    dNotes.add(no)

k = []
for key in keysNum:
    inKey = True
    for item in dNotes:
        if item not in keysNum[key]:
            inKey = False
            break
    if inKey:
        k.append(key)

if len(k) == 0 or len(k) > 1:
    print("cannot determine key")
else:
    print(k[0])
    for note in notes:
        print(keys[k[0]][keysNum[k[0]].index(note)])