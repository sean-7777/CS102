from main import LinkedList


l = LinkedList()

print("Add")
l.add(5)
print(l)

print("Add last")
l.addLast(7)
print(l)

print("Clear")
l.clear()
print(l)

print("Add multiple")
l.add(8)
l.add(9)
l.add(10)
l.add(11)
l.add(12)
print(l)

print("Contains")
print(l.contains(10))
print(l.contains(100))

print("Get")
print(l.get(0))
print(l.get(10))
print(l.get(2))

print("Get first/last")
print(l.getFirst())
print(l.getLast())

print("Size")
print(l.getSize())

print("Index of")
print(l.indexOf(10))
print(l.indexOf(100))
print(l.indexOf(8))

print("Insert")
l.insert(0, 1)
print(l)
l.insert(3, 1000)
print(l)

print("Is empty")
print(l.isEmpty())

print("Last index of")
l.addLast(47)
l.addLast(39)
l.addLast(40)
l.addLast(47)
print(l)
print(l.lastIndexOf(47))

print("Remove")
l.remove(47)
print(l)

print("Remove at")
l.removeAt(0)
print(l)

print("Remove first/last")
l.removeFirst()
print(l)
l.removeLast()
print(l)
