import linkedlist as l
import circularlinkedqueue as c
import doublylinkedlist as d

s = l.LinkedList()
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
print(s.display())
s.replace(2, 90)
print(s.display())

q = c.CircularLinkedQueue()
for i in range(8): q.enqueue(i)
print(q.display())

for i in range(5): q.dequeue()
print(q.display())
for i in range(8, 14): q.enqueue(i)
print(q.display())
