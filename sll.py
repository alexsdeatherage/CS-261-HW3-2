# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:



class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class SLNode:
    """
    Singly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with front and back sentinels
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.head = SLNode(None)
        self.tail = SLNode(None)
        self.head.next = self.tail

        # populate SLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.value)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
            length += 1
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.head.next == self.tail

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        Adds a new node at the beginning of the list (right after the front sentinel
        """

        current_node = SLNode(value)
        current_node.next = self.head.next
        self.head.next = current_node

    def add_back(self, value: object) -> None:
        """
        Adds a new node at the end of the list (right before the back sentinel).
        """
        # traverse the list to find last node
        self.rec_add_back(value, self.head.next)

    def rec_add_back(self, value: object, current_node: SLNode):
        """
        Recursive function for add_back
        """

        if self.is_empty():
            self.add_front(value)
            return

        elif current_node.next is self.tail:
            new_node = SLNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            return

        return self.rec_add_back(value, current_node.next)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        Adds a new value at the specified index position in the linked list. Index 0
        refers to the beginning of the list (right after the front sentinel).
        If the provided index is invalid, the method raises a custom “SLLException”
        """
        self.rec_insert_at_index(index, value, self.head, 0)

    def rec_insert_at_index(self, index: int, value: object, current_node: SLNode, counter: int):
        """
        Helper Function for insert_at_index
        """
        if index < 0 or index > self.length():
            raise SLLException()

        if index == 0:
            self.add_front(value)
            return

        if index == counter:
            new_node = SLNode(value)
            new_node.next = current_node.next
            current_node.next = new_node
            return

        return self.rec_insert_at_index(index, value, current_node.next, counter + 1)

    def remove_front(self) -> None:
        """
        Removes the first node from the list. If the list is empty, the method raises a
        custom “SLLException”.
        """
        if self.is_empty():
            raise SLLException()

        else:
            self.head.next = self.head.next.next

    def remove_back(self) -> None:
        """
        Removes the last node from the list. If the list is empty, the method raises a
        custom “SLLException”
        """
        self.rec_remove_back(self.head)

    def rec_remove_back(self, current_node):
        """
        Helper function for remove_back
        """
        if self.is_empty():
            raise SLLException()

        elif current_node.next.next is self.tail:
            current_node.next.next = None
            current_node.next = self.tail
            return

        return self.rec_remove_back(current_node.next)

    def remove_at_index(self, index: int) -> None:
        """
        Removes a node from the list given its index. Index 0 refers to the beginning of
        the list (right after the front sentinel.
        If the provided index is invalid, the method raises a custom “SLLException”
        """

        self.rec_remove_at_index(index, self.head, counter=0)

    def rec_remove_at_index(self, index: int, current_node: SLNode, counter: int):
        """
        Helper function for remove_at_index
        """
        if index < 0 or index > self.length() - 1:
            raise SLLException()

        if index == 0:
            self.remove_front()
            return

        if index == counter:

            prev_node = current_node
            current_node = current_node.next
            next_node = current_node.next

            prev_node.next = next_node
            return

        return self.rec_remove_at_index(index, current_node.next, counter + 1)

    def get_front(self) -> object:
        """
        Returns the value from the first node in the list without removing it. If the list is
        empty, the method raises a custom “SLLException”
        """
        if self.is_empty():
            raise SLLException()
        else:
            return self.head.next.value

    def get_back(self) -> object:
        """
        Returns the value from the last node in the list without removing it. If the list is
        empty, the method raises a custom “SLLException”.
        """
        return self.rec_get_back(self.head)

    def rec_get_back(self, current_node):
        """
        Helper function for get_back
        """
        if self.is_empty():
            raise SLLException()

        if current_node.next is self.tail:
            return current_node.value

        return self.rec_get_back(current_node.next)


    def remove(self, value: object) -> bool:
        """
        Traverses the list from the beginning to the end and removes the first node in
        the list that matches the provided “value” object. The method returns True if some node
        was actually removed from the list. Otherwise, it returns False
        """
        return self.rec_remove(value, self.head.next)

    def rec_remove(self, value, current_node=SLNode):
        """
        Helper function for remove
        """

        # If the node is at the start of the list
        if current_node.value == value:
            current_node.value = current_node.next.value
            current_node.next = current_node.next.next
            return True

        # If the node reaches the tail without finding the value
        if current_node.next is None:
            return False

        # If the node finds the value after the start of the list
        if current_node.next.value == value:
            current_node.next = current_node.next.next
            return True

        return self.rec_remove(value, current_node.next)


    def count(self, value: object) -> int:
        """
        Counts the number of elements in the list that match the provided “value”
        object.
        """
        return self.rec_count(value, self.head.next, counter=0)

    def rec_count(self, value: object, current_node, counter):
        """
        Helper function for count
        """
        if current_node is self.tail:
            return counter

        if current_node.value == value:
            return self.rec_count(value, current_node.next, counter + 1)

        else:
            return self.rec_count(value, current_node.next, counter)

    def slice(self, start_index: int, size: int) -> object:
        """
        Returns a new LinkedList object that contains the requested number of nodes
        from the original list starting with the node located at the requested start index.
        """
        new_LL = LinkedList(None)
        return self.rec_slice(start_index, size, self.head.next, new_LL, counter=0)

    def rec_slice(self, start_index: int, size: int, current_node, new_LL, counter):

        if size == 0:
            return new_LL

        # find where slice stops and is in bounds.
        if start_index < 0 or start_index > self.length() - 1:
            raise SLLException()

        if size > self.length():
            raise SLLException()

        if counter < start_index:
            counter += 1
            current_node = current_node.next

        if counter == start_index:
            new_LL.add_back(current_node.value)
            if new_LL.get_back() is None:
                raise SLLException()
            current_node = current_node.next
            if new_LL.length() == size:
                return new_LL

        return self.rec_slice(start_index, size, current_node, new_LL, counter)











if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # list = LinkedList()
    # print(list)
    # list.add_front('A')
    # list.add_front('B')
    # list.add_front('C')
    # print(list)
    #
    #
    # print('\n# add_back example 1')
    # list = LinkedList()
    # print(list)
    # list.add_back('C')
    # list.add_back('B')
    # list.add_back('A')
    # print(list)
    #
    #
    # print('\n# insert_at_index example 1')
    # list = LinkedList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         list.insert_at_index(index, value)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_front example 1')
    # list = LinkedList([1, 2])
    # print(list)
    # for i in range(3):
    #     try:
    #         list.remove_front()
    #         print('Successful removal', list)
    #     except Exception as e:
    #         print(type(e))
    #
    #
    # print('\n# remove_back example 1')
    # list = LinkedList()
    # try:
    #     list.remove_back()
    # except Exception as e:
    #     print(type(e))
    # list.add_front('Z')
    # list.remove_back()
    # print(list)
    # list.add_front('Y')
    # list.add_back('Z')
    # list.add_front('X')
    # print(list)
    # list.remove_back()
    # print(list)
    #
    #
    # print('\n# remove_at_index example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6])
    # print(list)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         list.remove_at_index(index)
    #         print(list)
    #     except Exception as e:
    #         print(type(e))
    # print(list)
    #
    #
    # print('\n# get_front example 1')
    # list = LinkedList(['A', 'B'])
    # print(list.get_front())
    # print(list.get_front())
    # list.remove_front()
    # print(list.get_front())
    # list.remove_back()
    # try:
    #     print(list.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    #
    # print('\n# get_back example 1')
    # list = LinkedList([1, 2, 3])
    # list.add_back(4)
    # print(list.get_back())
    # list.remove_back()
    # print(list)
    # print(list.get_back())
    #
    #
    # print('\n# remove example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(list)
    # for value in [7, 3, 3, 3, 3]:
    #     print(list.remove(value), list.length(), list)
    #
    #
    # print('\n# count example 1')
    # list = LinkedList([1, 2, 3, 1, 2, 2])
    # print(list, list.count(1), list.count(2), list.count(3), list.count(4))
    #
    #
    # print('\n# slice example 1')
    # list = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # ll_slice = list.slice(1, 3)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")

    # print('\n# slice example 1')
    # list = LinkedList([32783, 13507, -33144, 24285, -44272, 19701, 64384, 35541])
    # ll_slice = list.slice(8, 0)
    # print(list, ll_slice, sep="\n")
    # ll_slice.remove_at_index(0)
    # print(list, ll_slice, sep="\n")
    #
    #
    print('\n# slice example 2')
    list = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", list)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", list.slice(index, size))
        except:
            print(" --- exception occurred.")

