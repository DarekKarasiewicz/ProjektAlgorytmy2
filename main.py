import ast

file = open("test.txt", "r")

tmp = {}
tmp2 = {}
for x in file:
    for y in x:
        tmp[y] = 0
        tmp2[y] = 0
    for z in x:
        if z in tmp:
            tmp[z] = tmp.get(z) + 1
            tmp2[z] = tmp2.get(z) + 1

print(tmp)
class Node:
    def __init__(self, key =None):
        self.key  = key
        self.left = None
        self.right = None


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def min_heapify(arr, i, lenght):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left <= lenght and arr[largest] < arr[left]:
        largest = left

    if right <= lenght and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        min_heapify(arr, largest, lenght)


def build_min_hep(arr):
    lenght = len(arr)
    for i in range(((lenght - 1) // 2), -1, -1):
        min_heapify(arr, i, lenght - 1)


def heapsort(arr):
    build_min_hep(arr)
    lenght = len(arr)
    for i in range(lenght - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        lenght = lenght - 1
        min_heapify(arr, 0, lenght - 1)


def get_key(val,tmp):
    for key, value in tmp.items():
         if val == value:
             return key


keys=list(tmp.keys())
values=list(tmp.values())
print(values)
heapsort(values)
print(values)
print("-------------")
tmp1 = {}
while (len(values) >= 2):
    i = values.pop(0)
    a=get_key(i,tmp)
    tmp.pop(a)
    heapsort(values)
    j = values.pop(0)
    b=get_key(j,tmp)
    tmp.pop(b)
    c= str(a) + str(b)
    z = j + i
    tmp[c]=z
    tmp1[a]=i
    tmp1[b]=j
    tmp1[c]=z
    values.append(z)
    heapsort(values)
    print(values)
print(tmp)
print(tmp1)
print("_________________________")






values_tmp1=list(tmp1.values())
keys_tmp1=list(tmp1.keys())


tree = Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.left=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right.left=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right.right=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right.right.left=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right.right.right=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right.right.right.right=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))
tree.right.right.right.left=Node(keys_tmp1.pop()+":"+str(values_tmp1.pop()))

print(tree.display())
i=0
keys_tmp1=list(tmp1.keys())
keys_tmp2=list(tmp2.keys())
l=str(1)
while len(keys_tmp1) > 0:
    a=keys_tmp1.pop()
    for x in keys_tmp2:
        if a == x:
            tmp2[x]=l
    if i % 2 == 0:
         l=l+str(0)
    else:
        l=l[:-1]+str(1)
    i+=1


print(tmp2)
values_tmp2=list(tmp2.values())
my_code=""
file = open("test.txt", "r")
for x in file:
    for i in x:
        for n in tmp2:
            if n==i:
                my_code=my_code+tmp2[n]

my_code=my_code+"\n"+ str(tmp2)

with open('test_nowy.txt', 'w') as f:
    f.write(my_code)

file= open('test_nowy.txt', 'r')

print("----------------")
list_file=[]
for x in file:
    list_file.append(x)

dict_from_file=list_file.pop()
dict_file=ast.literal_eval(dict_from_file)
print(type(dict_file))
keys_dict=list(dict_file.keys())
values_dict=list(dict_file.values())

sum_string=""
result=""
code=list_file.pop().strip()

for x in code:
    sum_string+=x
    for i in values_dict:
        if (sum_string == i):
            key=get_key(i,dict_file)
            result+=key
            sum_string=""

print(result)
