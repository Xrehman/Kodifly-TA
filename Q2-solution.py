class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, n):
        first = self.head
        second = self.head
        for i in range(n):

            if (second.next == None):
                if (i == n - 1):
                    self.head = self.head.next
                return self.head
            second = second.next

        while (second.next != None):
            second = second.next
            first = first.next

        first.next = first.next.next

    def printList(self):
        tmp_head = self.head
        while (tmp_head != None):
            print(tmp_head.data, end=' ')
            tmp_head = tmp_head.next


head = [100, 2, 3, 4, 5]
n = 1
check = True
if len(head) <= 30 and len(head) >= 1:
    linked_lst = LinkedList()

    for i in range(len(head)):
        if head[len(head) - (i + 1)] <= 100 and head[len(head) - (i + 1)] >= 0:
            linked_lst.push(head[len(head) - (i + 1)])

        else:
            print('\n Please enter the values of node less than equal 100 or greater than equal to 0')
            check = False

    if check:
        print("\nIntial linked list:")
        linked_lst.printList()
        if n >= 1 and n <= len(head):
            linked_lst.deleteNode(n)
            print("\nFinal linked list:")
            linked_lst.printList()
        else:
            print('\nPlease enter the n value should be greater than equal to one and less then qual to size of linked list')


else:
    print('\nThe size of the linked list is less than equal to 30 or greater than eqaul to 1')

