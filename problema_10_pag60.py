a=set({"1","2","3","4"})
b=set({"1","2","3","4"})
for i in a:
    for j in a:
        b.add(i+j)
        for x in a:
            b.add(i+j+x)
            for y in a:
                b.add(i+j+x+y)
print(*b)