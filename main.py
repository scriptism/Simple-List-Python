# List operations and methods demonstration

li = ['fig', 'cherry', 'apple', 'date', 'elderberry', 'grape']
print(li) # or print(li[:])
# print(len(li))
print(li[2:6])
print(li[:4])
# print(li[3:])
# print(li[-4:-1])
# print(li[-3:])
if 'banana' in li:
    print(f"Yes, 'banana' is in the list at index {li.index('banana')}")
else:
    print("No, 'banana' is not in the list")
if 'apple' in li:
    print(f"Yes, 'apple' is in the list at index {li.index('apple')}")
else:
    print("No, 'apple' is not in the list")
li.append('kiwi')
if 'kiwi' in li:
    print(f"Yes, 'kiwi' is in the list at index {li.index('kiwi')}")
else:
    print("No, 'kiwi' is not in the list")
# insert, remove, pop
li.insert(1, 'blueberry')
# remove by value
li.remove('date')   
# pop the last element
# li.pop()
li.pop(3)  # pop by index
#  sort and reverse
li.sort()
# print(li)
# del li[4]
# del li[4:6]
# del li 
if 'apple' in li:
    print(f"Yes, 'apple' is in the list at index {li.index('apple')}")
else:
    print("No, 'apple' is not in the list")
# li.reverse()    
# print(li)
# li2 = li.copy()
# print(li2)
# li.clear()
# print(li)
tropical = ['mango', 'papaya', 'pineapple']
fruit_tuple = ('orange', 'watermelon', 'cantaloupe')
# append elements from another list to the current list
li.extend(tropical)
li.extend(fruit_tuple)
print(li)