
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
    size = [items[i][0] for i in items]
    value = [items[i][1] for i in items]
    return size, value

def get_memtable(items,A=8):
    size,value = size_and_value(items)
    n = len(value)
    keys = [i for i in items]
    V = [[0 for a in range(A+1)] for i in range(n+1)]
    for i in range(n+1):
        for a in range(A+1):
            if i==0 or a==0:
                V[i][a] = 0
            elif size[i-1]<=a:
                V[i][a] = max(value[i-1]+V[i-1][a-size[i-1]],V[i-1][a])
            else:
                V[i][a] = V[i-1][a]
    return V,size,value,keys


def get_selected_items_list(items, A=7):
    V, size, value, keys = get_memtable(items, A)
    n = len(value)
    a = A
    selected_stuff = []
    
    for i in range(n, 0, -1):
        if V[i][a] != V[i-1][a]:
            selected_stuff.append(keys[i-1])
            a -= size[i-1]
            
    return selected_stuff

backpack = get_selected_items_list(items)
total_value = sum(items[i][1] for i in backpack)
total_size = sum(items[i][0] for i in backpack)
all_items = sum(items[i][1] for i in items if items not in backpack)
newbag = []


for i in backpack:
    col = items[i][0]
    for j in range(col):
        newbag.append(i)


x = total_value+base_points-all_items+total_value
if x>0:
    print('существует')
else:
    print('такого решения нет')
print(x)