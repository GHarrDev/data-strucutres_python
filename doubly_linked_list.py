class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    message = None

    def push(self, data):
        node = Node(data, self.head)
        self.head = node
        return f"\nNode with value {data} was pushed to the head of the linked list."

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--> "
            itr = itr.next

        llstr += "END"
        print(llstr)

    def reverse_print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ""

        while itr.next:
            itr = itr.next
        
        while itr:
            llstr += str(itr.data) + " <--"
            itr = itr.prev

        llstr += "START"
        print(llstr)

    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return f"\nNode with value {data} was successfully appended to an empty linked list."
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next =Node (data, None)
        return f"\nNode with value {data} was successfully appended to the the linked list."

    def build(self, data_list):
        self.head = None
        count = 0
        for data in data_list:
            self.append(data)
            count += 1

        return f"\nLinked list of {count} elements successfully built."

    def length(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        message = f"Length: {length}"
        return length, message

    def print_length(self):
        length, message = ll.length()
        print(message)

    def insert(self, index, data):
        length, message = ll.length()
        if index < 0 or index >= length:
            raise Exception("Invalid index")
        
        if index == 0:
            self.push(data)
            return f"\nNode with value {data} was inserted at index {index}."
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node= Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
            return f"\nNode with value {data} was inserted at index {index}."

    def insert(self, index, data):
        length, message = self.length()
        if index < 0 or index > length:
            raise Exception("Invalid index")
        
        if index == 0:
            self.push(data)
            return f"\nNode with value {data} was inserted at index {index}."

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = itr.next
                itr.next = new_node
                return f"\nNode with value {data} was inserted at index {index}."
            itr = itr.next
            count += 1

    def insert_after_value(self, value, insert_value):
        if self.head is None:
            return f"\nNode with value {value} was not found in the list."
            
        itr = self.head
        found = False
        while itr:
            if itr.data == value:
                node = Node(insert_value, itr.next)
                itr.next = node
                found = True
                break
            
            itr = itr.next
        if not found:
            return f"\nNode with value {value} was not found in the list."
        else:
            return f"\nNode with value {insert_value} was successfully inserted after {value}"

    def delete(self, index):
        length, message = ll.length()
        if index < 0 or index >= length:
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return f"\nNode at index {index} has successfully been deleted from the linked list."
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
        return f"\nNode at index {index} has successfully been deleted from the linked list."

    def delete_by_value(self, data):
        if self.head.data == data:
            self.head = self.head.next
            return f"\nNode with value of {data} has been deleted from the linked list."
        
        itr = self.head
        found = False
        
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                found = True
            itr=itr.next

        if found:
            return f"\nNode with value of {data} has been deleted form the linked list."
        else:
            return f"\nNo Node with value of {data} found."
