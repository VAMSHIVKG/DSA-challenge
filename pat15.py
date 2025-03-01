#read number and represent it in the linked list form
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def ll(self,num):
        t=self.head
        while num!=0:
            val=num%10
            num=num//10
            new_node=Node(val)
            if not t:
                t=new_node
                




number=int(input())
num=reversed(str(number))
# head=None
while num!=0:
    val=num%10
    num=num//10
    new_node=Node(val)
    if not head:
        head=new_node
        prev=head
    else:
        prev.next=new_node
        prev=new_node
prev.next=None

# def show():
            