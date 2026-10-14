from itertools import combinations




items = {
    'r':(3,25),
    'p':(2,15),
    'a':(2,15),
    'm':(2,20),
    'k':(1,15),
    'x':(3,20),
    't':(1,25),
    'f':(1,15),
    's':(2,20),
    'c':(2,20),
    'i':(1,5),
    'd':(1,10)
}

base_points = 15

def size_and_value(items):
    keys = [i for i in items]
    size = [items[i][0] for i in items]
    value = [items[i][1] for i in items]
    return size, value,keys

size,value,keys = size_and_value(items)

maxA = 8
k = 1
for l in range(1,len(keys)+1):
    col  = combinations('rpamkxtfscid',r=l)
    for w in col:
        s = ''.join(w)
        total_size = 0
        total_value = 15
        for i in range(len(s)):
            total_value += items[s[i]][1]
            total_size += items[s[i]][0]
        if total_size<=8 and (2 * (total_value - 15) - 190) > 0:
            print(k,[x for x in s],"ценность:",(2 * (total_value - 15) - 190))
            k+=1