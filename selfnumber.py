x = set(range(1,10000))
remove_x = set()
li_x = list(x)
for i in li_x:
    num = 0
    num += i
    for k in range(0,len(str(i))):
        num += int(str(i)[k])
    remove_x.add(num)
y = x-remove_x
for t in sorted(y):
    print(t)