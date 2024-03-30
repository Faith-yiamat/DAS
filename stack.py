# accessing the top item without removing it (peeking)
stack = ["Faith","Yiamat","Yvonne","Martin"]
top_item = stack[-1]
print(top_item)

# accessing the top item and removing it
removing = stack.pop()
print(removing)

# removing the element in stack
remove_elem = stack.remove("Yvonne")
print(remove_elem)
print(stack)

# adding the elements to stack
add = stack.append("Oloserian")
print(add)
print(stack)
