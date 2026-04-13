lst=['Apple' , 'Banana' , 'Cherry', 'Date' , 'Honeydew' , 'Grape' ]
print("Length of list:", len(lst))
print("First item:", lst[0])
print("Last item:", lst[-1])

lst.append('Kiwi')
print("Updated list:", lst)

lst.remove('Date')
print("Updated list:", lst)

lst.sort()
print("Sorted list:", lst)

lst.pop()
print("Updated list:", lst)

lst.reverse()
print("Reversed list:", lst)

print("Multiplication of list:", lst*2)

lst=lst[:4]
print("Sliced list:", lst)
lst.clear()
print("Cleared list:", lst)