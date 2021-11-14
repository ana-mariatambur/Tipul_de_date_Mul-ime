a=set({"A","B","C","D"})
b=set({"A","B","C","D"})
for i in a:
    for j in a:
        b.add(i+j)
        for x in a:
            b.add(i+j+x)
            for y in a:
                b.add(i+j+x+y)
print(*b)