

#list store multiple items in single variables
#Lists are created using square brackets

#create list
items=["bread","jam","pasta"]
print(items)


#access list items
items=["fruits","vegetable","bread","oil"]
print(items[0])

print(items[3])

#modify list 
#instead of fruits add chips
items[0]='chips'
print(items)

#acces range of element
print(items[1:4])
#print last element by negative index
print(items[-1])

#append
items.append("butter")
print(items)

#insert element at specific location
items.insert(1,'cheese')
print(items)

#join list
food=["maggie","noodles"]
bathroom=["shampoo","soap"]
items=food+bathroom
print(items)

#to know how many items i buy
print(len(items))

#check items list
print("bread" in items)
print("maggie" in items)









