class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    # Insert at position. If no position arg given, insert at end.
    def insert(self,val,pos=None):
        if pos is None: pos = self.length
        if pos > self.length:
            print(f"[ERROR] Insert position > length of list. No action taken.")
        elif pos <= self.length:
            new_node = Node(val)
            if self.root is None:
                self.root = new_node
            elif self.root is not None and pos is 0:
                new_node.next = self.root
                self.root = new_node
            elif self.root is not None and pos is not 0:
                working_node = self.root
                for _ in range(pos-1): working_node = working_node.next
                new_node.next = working_node.next
                working_node.next = new_node
            self.length+=1

    def pop(self,pos=None):
        if pos is None: pos = self.length-1
        if pos > self.length:
            print(f"[ERROR] Remove position > length of list. No action taken.")
        elif pos <= self.length:
            if self.root is not None and pos is 0:
                removal_node = self.root
                self.root = self.root.next
                del removal_node
            elif self.root is not None and pos is not 0 and pos is not self.length:
                working_node = self.root
                for _ in range(pos-1): working_node = working_node.next
                removal_node = working_node.next
                working_node.next = removal_node.next
                del removal_node


    def print_list(self):
        if self.root is None:
            print("[]")
        elif self.root is not None:
            working_node = self.root
            print("[",end="")
            while working_node.next is not None:
                print(str(working_node.data)+",",end="")
                working_node = working_node.next
            print(str(working_node.data)+"]")

