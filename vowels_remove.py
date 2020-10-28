text = input('enter text : ')
d = {i:0 for i in 'aeiou'}
vowels = []
for char in text:
    if char in d:
        d[char] += 1
for i,j in d.items():
    vowels.append(i)
    print(i,j)
new_text = [i for i in text if i not in vowels]
print(''.join(new_text))