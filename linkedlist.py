# create a linked list of 3 elements and display them
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class ll:
    def show(head):
        t=head
        while(t):
            print(t.data,end=',')
            t=t.next


##find duplicates in the linked list
    def find_dup(head):
        t=set()
        flag=1
        h=head
        # dup=[]
        while h:
            if h.data in t:
                print(h.data, "is duplicate")
                return
            else:
                t.add(h.data)
            h=h.next
        if flag==1:
                print("no duplicate data")
                flag=0
        # return dup



##adding the data into the linked list by static method
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(20)
head.next.next.next.next=Node(30)
obj=ll
a=obj.show(head)
print(a)

##calling dupicate function
obj.find_dup(head)