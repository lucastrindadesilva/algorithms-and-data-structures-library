from heap import MinHeap, MaxHeap


############## tests cases         
heap = MinHeap()   

print("Inserting 2 to Minheap")
heap.insert((2,"Ana"))
print("MinHeap = {}".format(heap))

print("Inserting 7 to Minheap")
heap.insert((7,"José"))
print("MinHeap = {}".format(heap))

print("Inserting 26 to Minheap")
heap.insert((26,"Valdir"))
print("MinHeap = {}".format(heap))

print("Inserting 25 to Minheap")
heap.insert((25,"Ubaldo"))
print("MinHeap = {}".format(heap))

print("Inserting 19 to Minheap")
heap.insert((19,"Ofélia"))
print("MinHeap = {}".format(heap))

print("removed: {}".format(heap.remove()))
print("MinHeap = {}".format(heap))

print("removed: {}".format(heap.remove()))
print("MinHeap = {}".format(heap))

#######

heap = MaxHeap()   

print("Inserting 2 to Maxheap")
heap.insert((2,"Ana"))
print("MaxHeap = {}".format(heap))

print("Inserting 7 to Maxheap")
heap.insert((7,"José"))
print("MaxHeap = {}".format(heap))

print("Inserting 26 to Maxheap")
heap.insert((26,"Valdir"))
print("MaxHeap = {}".format(heap))

print("Inserting 25 to Maxheap")
heap.insert((25,"Ubaldo"))
print("MaxHeap = {}".format(heap))

print("Inserting 19 to Maxheap")
heap.insert((19,"Ofélia"))
print("MaxHeap = {}".format(heap))

print("removed: {}".format(heap.remove()))
print("MaxHeap = {}".format(heap))

print("removed: {}".format(heap.remove()))
print("MaxHeap = {}".format(heap))