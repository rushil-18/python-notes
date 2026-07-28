word = input("Enter the string: ")
count = {}
for char in word:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1
repeating = []
for char in count:
    if count[char] > 1:
        repeating.append(char)

third = repeating[2]

print("3rd repeating character:", third)
print("Number of repetitions:", count[third])