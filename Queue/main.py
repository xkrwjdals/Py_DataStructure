import deck as d
import circuluarQueue as cq
import priorityqueue as pq

print("원형 큐 테스트")
q = cq.CirculuarQueue(10)
print("Circular Queue : Max Size 10")
for i in range(8): q.enqueue(i)
print("enqueue 8번")
q.display()
for i in range(5): q.dequeue()
print("dequeue 5번")
q.display()
for i in range(8, 14): q.enqueue(i)
print("enqueue 6번")
q.display()

print("\n덱 테스트")
dq = d.CircularDeque(10)
print("Deck : Max Size 10")
for i in range(9):
    if i%2==0: dq.addRear(i)
    else: dq.addFront(i)
print("짝수 : add Rear, 홀수 : add Front")
dq.display()
for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
print("delete Front 2번, delete Rear 3번")
dq.display()
for i in range(9, 14): dq.addFront(i)
print("add Front 5번")
dq.display()

print("\n우선순위 큐 테스트")
pq = pq.PriorityQueue()
pq.enqueue(34)
pq.enqueue(18)
pq.enqueue(27)
pq.enqueue(45)
pq.enqueue(15)
print("PQueue:", pq.list)
while not pq.isEmpty():
    print("Max Priority = ", pq.dequeue())