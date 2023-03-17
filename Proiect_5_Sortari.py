import random
#print(random.randint(a, b)) -generates an integer number a <= random.randint(a, b) <= b
import sys
sys.setrecursionlimit(10000)
import time
import tracemalloc

# test_sort(lista) -testeaza daca lista de numere naturale este sortata crescator.
def test_sort(Ls):
    for i in range(len(Ls) - 1):
        if Ls[i] > Ls[i + 1]:
            return False
    return True


# 1 RadixSort(lista, base)
def copy_back(a, v):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            v[count] = a[i][j]
            count += 1

def RadixSort(v, base):
    if base + len(v) > 2 * (10**8):
        print("RADIXSORT nu poate sorta (eficient)!")
        return
    bs = []
    placement = 1
    nr = len(str(max(v)))
    while nr > 0:
        bs = [[] for i in range(base)]
        for i in range(len(v)):
            bs[(v[i] // placement) % base].append(v[i])
        copy_back(bs, v)
        placement *= base
        bs.clear()
        nr -= 1


# 2 MergeSort(lista, left, right)
def Merge(v, left, mid, right):
    i = left
    j = mid + 1
    L1 = []
    while i <= mid and j <= right:
        if v[i] <= v[j]:
            L1.append(v[i])
            i += 1
        else:
            L1.append(v[j])
            j += 1
    while i <= mid:
        L1.append(v[i])
        i += 1
    while j <= right:
        L1.append(v[j])
        j += 1
    v[left:right + 1] = L1[:]

def Merge_sort(v, left, right):
    if left < right:
        mid = left + ((right - left) >> 1)
        Merge_sort(v, left, mid)
        Merge_sort(v, mid + 1, right)
        Merge(v, left, mid, right)

def MergeSort(Ls):
    if len(Ls) > 10**7:
        print("MERGESORT nu poate sorta rapid si/sau utilizeaza prea multa memorie suplimentara!")
        return
    n = len(Ls)
    Merge_sort(Ls, 0, n - 1)


# 3 CountSort(lista)
def CountSort(L):
    maxim = 0
    for x in L:
        if x > maxim:
            maxim = x
    if maxim + len(L) > 2 * (10**8):
        print("COUNTSORT nu poate sorta (eficient)!")
        return 
    Fr = [0] * (maxim + 1)
    for x in L:
        Fr[x] += 1
    ct = 0
    for i in range(len(Fr)):
        while Fr[i] > 0:
            L[ct] = i
            ct += 1
            Fr[i] -= 1


# 4 HeapSort(lista)
def Heapify(v, start, end):
    flag = True
    while flag:
        maxpos = start
        left = (start << 1) + 1
        right = left + 1
        if left < end and v[left] > v[maxpos]:
            maxpos = left
        if right < end and v[right] > v[maxpos]:
            maxpos = right
        if maxpos != start:
            v[start], v[maxpos] = v[maxpos], v[start]
            start = maxpos
        else:
            flag = False

def HeapSort(Ls):
    ln = len(Ls)
    if ln > 10**7:
        print("HEAPSORT nu poate sorta rapid!")
        return
    for i in range((ln - 1) >> 1, -1, -1):
        Heapify(Ls, i, ln)
    for i in range(ln - 1, -1, -1):
        Ls[0], Ls[i] = Ls[i], Ls[0]
        Heapify(Ls, 0, i)

# 5 ShellSort(lista)
def ShellSort(Ls):
    ln = len(Ls)
    if ln > 10**6:
        print("SHELLSORT nu poate sorta rapid!")
        return
    space = ln >> 1
    while space > 0:
        i = space
        while i < ln:
            aux = Ls[i]
            k = i
            while k >= space and Ls[k - space] > aux:
                Ls[k] = Ls[k - space]
                k -= space
            Ls[k] = aux
            i += 1
        space = space >> 1

###
def Sorts(Nume, L):
    tracemalloc.start()
    start = time.time()
    Nume(L)
    stop = time.time()
    print(f"Memory used: {tracemalloc.get_traced_memory()}")
    print(f"Time: {stop - start}")
    print(test_sort(L))
    print("\n\n")
    tracemalloc.stop()

def Radix_base(Radix, L, base):
    tracemalloc.start()
    start = time.time()
    Radix(L, base)
    stop = time.time()
    print(f"Memory used: {tracemalloc.get_traced_memory()}")
    print(f"Time: {stop - start}")
    print(test_sort(L))
    print("\n\n")
    tracemalloc.stop()

def NativeSort(L):
    tracemalloc.start()
    start = time.time()
    L.sort()
    stop = time.time()
    print(f"Memory used: {tracemalloc.get_traced_memory()}")
    print(f"Time: {stop - start}")
    print(test_sort(L))
    print("\n\n")
    tracemalloc.stop()

#MAIN:

Tests = [(10**3, 10**3), (10**3, 10**6), (10**3, 10**8), (10**6, 10**3), (10**6, 10**6), 
         (10**6, 10**8), (10**7, 10**3), (10**7, 10**6), (10**7, 10**8), (10**8, 10**8)]


#st = 0
#dr = len(Tests)
st = 2
dr = st + 1
for i in range(st, dr):
    print(f"N = {Tests[i][0]}")
    print(f"Max = {Tests[i][1]}")
    print()
    L = []
    ###
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("RadixSort, base 10:\n")
    Radix_base(RadixSort, L, 10)
    L.clear()
    #
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("RadixSort, base 2^16:\n")
    Radix_base(RadixSort, L, 2**16)
    L.clear()
    ##
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("MergeSort:\n")
    Sorts(MergeSort, L)
    L.clear()
    #
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("CountSort:\n")
    Sorts(CountSort, L)
    L.clear()
    #
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("HeapSort:\n")
    Sorts(HeapSort, L)
    L.clear()
    #
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("ShellSort:\n")
    Sorts(ShellSort, L)
    L.clear()
    ##
    for j in range(Tests[i][0]):
        L.append(random.randint(0, Tests[i][1]))
    print("Algoritm de sortare nativ al limbajului Python(TimSort):\n")
    NativeSort(L)
    L.clear()
    #




"""
Ldd = []
Ldd.append(1)
Ldd.append(4)
Ldd.append(89)
print(Ldd)
Ldd.clear()
print(Ldd)
Ldd.append(12)
Ldd.append(7)
Ldd.append(12)
Ldd.append(7)
Ldd.append(11)
Ldd.append(3)
Ldd.append(19)
Ldd.append(700)
print(Ldd)
Ldd.clear()
print(Ldd)
Ldd.append(1000)
print(Ldd)
"""



