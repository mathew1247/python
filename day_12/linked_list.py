class node:
    def __init__(self,data):
        self.data = data
        self.next = None
newnode=node(10)
newnode_1 = node(20)
newnode_2 =node(30)
newnode.next=newnode_1
newnode_1.next = newnode_2
print(newnode.data)
print(newnode.next.data)
print(newnode.next.next.data)

def length_of_list(newnode):
    temp = newnode 
    count =0
    while temp is not None:
        count =count+1
        temp=temp.next
    return count
print(length_of_list(newnode))

##--------------------------------------------##
## Traversing a linked list
temp = newnode
while temp is not None:
    print(temp.data)
    temp=(temp.next)

##--------------------------------------------##
