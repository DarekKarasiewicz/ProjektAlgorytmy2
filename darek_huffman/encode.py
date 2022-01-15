from darek_huffman.util import get_key

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

def encode(clear_text):
    dist = {}    
    huffman_code={}
    for x in clear_text:
        dist[x] = dist.get(x,0)+1
        huffman_code[x] = huffman_code.get(x,0)+1

    
    keys=list(dist.keys())
    values=list(dist.values())
    heapsort(values)
    sub_dist = {}
    while (len(values) >= 2):
        i = values.pop(0)
        a=get_key(i,dist)
        dist.pop(a)
        heapsort(values)
        j = values.pop(0)
        b=get_key(j,dist)
        dist.pop(b)
        c= str(a) + str(b)
        z = j + i
        dist[c]=z
        sub_dist[a]=i
        sub_dist[b]=j
        sub_dist[c]=z
        values.append(z)
        heapsort(values)
    
    i=0
    keys_tmp1=list(sub_dist.keys())
    keys_tmp2=list(huffman_code.keys())
    l=str(1)
    while len(keys_tmp1) > 0:
        a=keys_tmp1.pop()
        for x in keys_tmp2:
            if a == x:
                huffman_code[x]=l
        if i % 2 == 0:
             l=l+str(0)
        else:
            l=l[:-1]+str(1)
        i+=1
    

    values_tmp2=list(huffman_code.values())
    my_code=""
    for x in clear_text:
        for i in x:
            for n in huffman_code:
                if n==i:
                    my_code=my_code+huffman_code[n]

    #my_code=my_code+"\n"+ str(huffman_code)

    return my_code,huffman_code

