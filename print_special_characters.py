text = 'hello world @ 123'
l = []
for i in text:
    if not i.isalnum() and i != ' ':
        l.append(i)
print(l)
