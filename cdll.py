# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class CDLLException(Exception):
    """
    Custom exception class to be used by Circular Doubly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DLNode:
    """
    Doubly Linked List Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a new linked list with sentinel
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.sentinel = DLNode(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate CDLL with initial values (if provided)
        # before using this feature, implement add_back() method
        if start_list is not None:
            for value in start_list:
                self.add_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'CDLL ['
        if self.sentinel.next != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.value)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.value)
                cur = cur.next
        out = out + ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list

        This can also be used as troubleshooting method. This method works
        by independently measuring length during forward and backward
        traverse of the list and return the length if results agree or error
        code of -1 or -2 if thr measurements are different.

        Return values:
        >= 0 - length of the list
        -1 - list likely has an infinite loop (forward or backward)
        -2 - list has some other kind of problem

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # length of the list measured traversing forward
        count_forward = 0
        cur = self.sentinel.next
        while cur != self.sentinel and count_forward < 101_000:
            count_forward += 1
            cur = cur.next

        # length of the list measured traversing backwards
        count_backward = 0
        cur = self.sentinel.prev
        while cur != self.sentinel and count_backward < 101_000:
            count_backward += 1
            cur = cur.prev

        # if any of the result is > 100,000 -> list has a loop
        if count_forward > 100_000 or count_backward > 100_000:
            return -1

        # if counters have different values -> there is some other problem
        return count_forward if count_forward == count_backward else -2

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.sentinel.next == self.sentinel

    # ------------------------------------------------------------------ #

    def add_front(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        # Creates the new node
        new_node = DLNode(value)

        # Links the new node to its previous and next links
        new_node.prev = self.sentinel
        new_node.next = self.sentinel.next

        # New node follows the Front Sentinel
        self.sentinel.next = new_node

        # Previous node of its next node
        new_node.next.prev = new_node
        return

    def add_back(self, value: object) -> None:
        """
        TODO: Write this implementation
        """
        last_node = self.sentinel.prev
        new_node = DLNode(value)

        new_node.prev = last_node
        new_node.next = last_node.next

        last_node.next = new_node

        new_node.next.prev = new_node

    def insert_at_index(self, index: int, value: object) -> None:
        """
        TODO: Write this implementation
        """
        if index < 0 or index > self.length():
            raise CDLLException()

        if index == 0:
            self.add_front(value)
            return

        counter = 0
        current_node = self.sentinel

        while counter <= index:
            current_node = current_node.next
            counter += 1

        previous_node = current_node.prev
        new_node = DLNode(value)
        new_node.prev = previous_node
        new_node.next = current_node

        current_node.prev = new_node
        previous_node.next = new_node
        return

    def remove_front(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException()

        else:
            node = self.sentinel.next

            node.prev.next = node.next
            node.next.prev = node.prev

    def remove_back(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException()

        else:
            last_node = self.sentinel.prev

            last_node.prev.next = last_node.next
            last_node.next.prev = last_node.prev

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        counter = 0
        current_node = self.sentinel.next

        if index < 0 or index > self.length() - 1:
            raise CDLLException()

        if index == 0:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            return

        while counter <= index:
            current_node = current_node.next
            counter += 1
            if counter == index:
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                return

    def get_front(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException()
        else:
            return self.sentinel.next.value

    def get_back(self) -> object:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            raise CDLLException()
        else:
            return self.sentinel.prev.value

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """

        current_node = self.sentinel.next
        found = False

        while current_node and not found:
            if current_node.value == value and current_node is self.sentinel.next:
                self.remove_front()
                return True
            elif current_node.value == value:
                previous_node = current_node.prev
                next_node = current_node.next
                previous_node.next = next_node
                next_node.prev = previous_node
                return True
            elif current_node.next.value is None:
                return False
            else:
                current_node = current_node.next

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        counter = 0
        current_node = self.sentinel.next
        while current_node.value is not None:
            if current_node.value == value:
                counter += 1
                current_node = current_node.next
            else:
                current_node = current_node.next

        return counter

    def swap_pairs(self, index1: int, index2: int) -> None:
        """
        TODO: Write this implementation
        """

        length = self.length()

        first_index = min(index1, index2)
        last_index = max(index1, index2)
        left_index = 0
        right_index = length - 1

        if first_index < 0 or first_index > length - 1:
            raise CDLLException()

        if last_index < 0 or last_index > length - 1:
            raise CDLLException()

        if index1 == index2:
            return

        left_node = self.sentinel.next
        right_node = self.sentinel.prev

        while left_index != first_index or right_index != last_index:
            if left_index != first_index:
                left_node = left_node.next
                left_index += 1

            if right_index != last_index:
                right_node = right_node.prev
                right_index -= 1

        if abs(right_index - left_index) == 1:
            # 0 <> 1 <> 2 <> 3
            # left_node = 1
            # right_node = 2
            left_of_left_none = left_node.prev
            right_of_right_node = right_node.next

            left_of_left_none.next = right_node  # 0 -> 2
            right_node.prev = left_of_left_none  # 0 <- 2

            right_node.next = left_node  # 2 -> 1
            left_node.prev = right_node  # 1 -> 2

            left_node.next = right_of_right_node  # 1 -> 3
            right_of_right_node.prev = left_node  # 3 -> 1

        else:
            left_of_left_node = left_node.prev
            right_of_left_node = left_node.next

            left_of_right_node = right_node.prev
            right_of_right_node = right_node.next

            left_of_left_node.next = left_node.next
            right_of_left_node.prev = left_node.prev
            left_node.next = left_node.prev

            left_of_right_node.next = right_node.next
            right_of_right_node.prev = right_node.prev
            right_node.next = right_node.prev

            left_node.prev = right_node.prev
            right_node.prev = left_node.next

            left_node.next = left_node.prev
            right_node.next = right_node.prev

            left_node.next = left_node.next.next
            left_node.next.prev = left_node
            left_node.prev.next = left_node

            right_node.next = right_node.next.next
            right_node.next.prev = right_node
            right_node.prev.next = right_node

            # Assigns the pointers of the left node
            left_node.prev = left_of_right_node
            left_node.next = right_of_right_node

            right_of_left_node.prev = right_node
            left_of_left_node.next = right_node

            # Assigns the pointers of the right node
            right_node.prev = left_of_left_node
            right_node.next = right_of_left_node

            left_of_right_node.next = left_node
            right_of_right_node.prev = left_node

    def reverse(self) -> None:
        """
        TODO: Write this implementation
        """

        current_node = self.sentinel.prev

        length = self.length() - 1
        counter = 0
        temp = None

        while counter <= length:
            counter += 1
            temp = current_node.next
            current_node.next = current_node.prev  # SS -> 0
            current_node.prev = temp  # SS <- 0

            current_node = current_node.next

        temp2 = self.sentinel.next
        self.sentinel.next = self.sentinel.prev
        self.sentinel.prev = temp2

        # print(self.sentinel.next.value)
        # print(self.sentinel.prev.value)
        # print(self.sentinel.next.next.value)

    def sort(self) -> None:
        """
        TODO: Write this implementation
        """
        if self.is_empty():
            return

    def rotate(self, steps: int) -> None:
        """
        TODO: Write this implementation
        """

        length = self.length()
        if steps == 0 or self.is_empty():
            return

        positive_dir = True
        if steps < 0:
            positive_dir = False

        new_steps = steps % length

        current_node = self.sentinel

        if positive_dir:
            for i in range(new_steps):
                current_node = current_node.prev
        else:
            for i in range(new_steps):
                current_node = current_node.prev

        tracker = current_node

        if tracker is self.sentinel:
            return

        self.sentinel.next.prev = self.sentinel.prev
        self.sentinel.prev.next = self.sentinel.next

        prev_tracker = current_node.prev
        prev_tracker.next = self.sentinel
        self.sentinel.prev = prev_tracker

        self.sentinel.next = tracker
        tracker.prev = self.sentinel

    def remove_duplicates(self) -> None:
        """
        TODO: Write this implementation
        """

        if self.is_empty():
            return

        duplicate = None
        length = self.length()
        lead_pointer = self.sentinel.next
        trail_pointer = self.sentinel

        for _ in range(length):
            lead_value = lead_pointer.value
            lead_pointer = lead_pointer.next

            if lead_value == lead_pointer.value:
                duplicate = True

            else:
                # pass through duplicates
                if duplicate is not True:
                    trail_pointer = trail_pointer.next
                else:
                    trail_pointer.next = lead_pointer
                    lead_pointer.prev = trail_pointer
                    duplicate = False

    def odd_even(self) -> None:
        """
        TODO: Write this implementation
        """
        pass
        # if self.is_empty():
        #     return
        #
        # if self.sentinel.next.next is self.sentinel:
        #     return
        #
        # # Index starts at 1
        # trail = self.sentinel.next
        # lead = self.sentinel.next.next
        # index = 1
        #
        # while lead.next is not self.sentinel:
        #     index += 1
        #     if index % 2 == 0:
        #         lead = lead.next
        #     else:
        #         print(1)
        # change pointers against to two nodes swapping
        # change nodes that are going to be swapped
        # swap1 = lead.next # 3
        # trail.next.prev = swap1
        # swap1.next = trail.next
        # swap1.prev = trail
        # trail.next = swap1
        #
        # swap1.prev.next = swap1.next
        # swap1.next.prev = swap1.prev
        #
        # trail = trail.next
        # print(swap1.value)

    def add_integer(self, num: int) -> None:
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':
    pass

    # print('\n# add_front example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_front('A')
    # lst.add_front('B')
    # lst.add_front('C')
    # print(lst)

    # print('\n# add_back example 1')
    # lst = CircularList()
    # print(lst)
    # lst.add_back('C')
    # lst.add_back('B')
    # lst.add_back('A')
    # print(lst)
    #
    # print('\n# insert_at_index example 1')
    # lst = CircularList()
    # test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    # for index, value in test_cases:
    #     print('Insert of', value, 'at', index, ': ', end='')
    #     try:
    #         lst.insert_at_index(index, value)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_front example 1')
    # lst = CircularList([1, 2])
    # print(lst)
    # for i in range(3):
    #     try:
    #         lst.remove_front()
    #         print('Successful removal', lst)
    #     except Exception as e:
    #         print(type(e))
    #
    # print('\n# remove_back example 1')
    # lst = CircularList()
    # try:
    #     lst.remove_back()
    # except Exception as e:
    #     print(type(e))
    # lst.add_front('Z')
    # lst.remove_back()
    # print(lst)
    # lst.add_front('Y')
    # lst.add_back('Z')
    # lst.add_front('X')
    # print(lst)
    # lst.remove_back()
    # print(lst)
    #
    # print('\n# remove_at_index example 1')
    # lst = CircularList([1, 2, 3, 4, 5, 6])
    # print(lst)
    # for index in [0, 0, 0, 2, 2, -2]:
    #     print('Removed at index:', index, ': ', end='')
    #     try:
    #         lst.remove_at_index(index)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))
    # print(lst)
    #
    # print('\n# get_front example 1')
    # lst = CircularList(['A', 'B'])
    # print(lst.get_front())
    # print(lst.get_front())
    # lst.remove_front()
    # print(lst.get_front())
    # lst.remove_back()
    # try:
    #     print(lst.get_front())
    # except Exception as e:
    #     print(type(e))
    #
    # print('\n# get_back example 1')
    # lst = CircularList([1, 2, 3])
    # lst.add_back(4)
    # print(lst.get_back())
    # lst.remove_back()
    # print(lst)
    # print(lst.get_back())
    #
    # print('\n# remove example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(lst)
    # for value in [7, 3, 3, 3, 3]:
    #     print(lst.remove(value), lst.length(), lst)
    #
    # print('\n# count example 1')
    # lst = CircularList([1, 2, 3, 1, 2, 2])
    # print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))
    #
    # print('\n# swap_pairs example 1')
    # lst = CircularList([0, 1, 2, 3, 4, 5, 6])
    # test_cases = ((0, 6), (0, 7), (-1, 6), (1, 5),
    #               (4, 2), (3, 3), (1, 2), (2, 1))
    #
    # for i, j in test_cases:
    #     print('Swap nodes ', i, j, ' ', end='')
    #     try:
    #         lst.swap_pairs(i, j)
    #         print(lst)
    #     except Exception as e:
    #         print(type(e))

    print('\n# reverse example 1')
    test_cases = (
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 4, 5],
        ['A', 'B', 'C', 'D']
    )
    for case in test_cases:
        lst = CircularList(case)
        lst.reverse()
        print(lst)

    print('\n# reverse example 2')
    lst = CircularList()
    print(lst)
    lst.reverse()
    print(lst)
    lst.add_back(2)
    lst.add_back(3)
    lst.add_front(1)
    lst.reverse()
    print(lst)

    print('\n# reverse example 3')


    class Student:
        def __init__(self, name, age):
            self.name, self.age = name, age

        def __eq__(self, other):
            return self.age == other.age

        def __str__(self):
            return str(self.name) + ' ' + str(self.age)


    s1, s2 = Student('John', 20), Student('Andy', 20)
    lst = CircularList([s1, s2])
    print(lst)
    lst.reverse()
    print(lst)
    print(s1 == s2)

    print('\n# reverse example 4')
    lst = CircularList([1, 'A'])
    lst.reverse()
    print(lst)
    #
    # print('\n# sort example 1')
    # test_cases = (
    #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    #     [(1, 1), (20, 1), (1, 20), (2, 20)]
    # )
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print(lst)
    #     lst.sort()
    #     print(lst)
    #
    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # for steps in [1, 2, 0, -1, -2, 28, -100]:
    #     lst = CircularList(source)
    #     lst.rotate(steps)
    #     print(lst, steps)
    #
    # print('\n# rotate example 2')
    # lst = CircularList([10, 20, 30, 40])
    # for j in range(-1, 2, 2):
    #     for _ in range(3):
    #         lst.rotate(j)
    #         print(lst)
    #
    # print('\n# rotate example 3')
    # lst = CircularList()
    # lst.rotate(10)
    # print(lst)
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], [1, 1, 1, 1, 1],
    #     [], [1], [1, 1], [1, 1, 1, 2, 2, 2],
    #     [0, 1, 1, 2, 3, 3, 4, 5, 5, 6],
    #     list("abccd"),
    #     list("005BCDDEEFI")
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.remove_duplicates()
    #     print('OUTPUT:', lst)
    #
    # print('\n# odd_even example 1')
    # test_cases = (
    #     [1, 2, 3, 4, 5], list('ABCDE'),
    #     [], [100], [100, 200], [100, 200, 300],
    #     [100, 200, 300, 400],
    #     [10, 'A', 20, 'B', 30, 'C', 40, 'D', 50, 'E']
    # )
    #
    # for case in test_cases:
    #     lst = CircularList(case)
    #     print('INPUT :', lst)
    #     lst.odd_even()
    #     print('OUTPUT:', lst)

    # print('\n# add_integer example 1')
    # test_cases = (
    #   ([1, 2, 3], 10456),
    #   ([], 25),
    #   ([2, 0, 9, 0, 7], 108),
    #    ([9, 9, 9], 9_999_999),
    # )
    # for list_content, integer in test_cases:
    #    lst = CircularList(list_content)
    # print('INPUT :', lst, 'INTEGER', integer)
    # lst.add_integer(integer)
    # print('OUTPUT:', lst)
