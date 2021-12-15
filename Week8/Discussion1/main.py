"""
  CS102 - Programming Assignment 7
  18.3 - Implement Linked List
  Sean X.
  Tuesday, Dec. 14, 2021

  Summary
    Implementation of a Linked List.
"""

from __future__ import annotations

from typing import Any


class Node:
    """A node in a linked list

    Attributes:
        value: The value of the node
        next: The next node in the list
    """

    def __init__(self, value: Any, nextNode: Node | None = None):
        self.value: Any = value
        self.next: Node | None = nextNode


class LinkedList:
    """A linked list"""

    # Tl;DR: My type checker can't find the link
    # between self.__size with self.__tail and self.__head

    # In some methods I have things like:
    # if self.__size == 0 or self.__head is None:
    # because my type checker doesn't like it if I don't check for the head or tail
    # variables are none and use them like a type: Node instead of type: Node | None

    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None
        self.__size: int = 0

    def getFirst(self) -> None | Any:
        """Get the first element in the list"""

        if self.__size == 0 or self.__head is None:
            return None

        return self.__head.value

    def getLast(self) -> None | Any:
        """Get the last element in the list"""

        if self.__size == 0 or self.__tail is None:
            return None

        return self.__tail.value

    def addFirst(self, value: Any) -> None:
        """Add an element to the front of the list

        Arguments:
            value: The element to add
        """

        self.__head = Node(value, self.__head)
        self.__size += 1

        if self.__tail is None:
            self.__tail = self.__head

    def addLast(self, value: Any) -> None:
        """Add an element to the end of the list

        Arguments:
            value: The element to add
        """

        if self.__tail is None:
            self.__head = self.__tail = Node(value)
        else:
            self.__tail.next = Node(value)
            self.__tail = self.__tail.next

        self.__size += 1

    add = addLast

    def insert(self, index: int, value: Any) -> None:
        """Insert an element at the specified position in this list.

        Arguments:
            index: The index at which the specified element is to be inserted
            value: The element to be inserted
        """

        if index == 0:
            self.addFirst(value)
        elif index >= self.__size:
            self.addLast(value)
        else:
            current: Node = self.__head  # type: ignore
            for _ in range(index - 1):
                current = current.next  # type: ignore

            current.next = Node(value, current.next)

            self.__size += 1

    def removeFirst(self) -> Any:
        """Remove the first element from the list"""

        if self.__size == 0 or self.__head is None:
            return None

        before: Node = self.__head
        self.__head = self.__head.next
        self.__size -= 1

        if self.__head is None:
            self.__tail = None

        return before.value

    def removeLast(self):
        """Remove the last element from the list"""

        if self.__size == 0 or self.__head is None or self.__tail is None:
            return None

        if self.__size == 1:
            before: Node = self.__head
            self.__head = self.__tail = None
            self.__size = 0
            return before.value

        current = self.__head
        for _ in range(self.__size - 2):
            current: Node = current.next  # type: ignore

        before: Node = self.__tail
        self.__tail = current
        self.__tail.next = None
        self.__size -= 1
        return before.value

    def removeAt(self, index: int) -> Any:
        """Remove the element at the specified position in this list.

        Arguments:
            index: The index of the element to remove
        """

        if index < 0 or index >= self.__size or self.__head is None:
            return None

        if index == 0:
            return self.removeFirst()

        if index == self.__size - 1:
            return self.removeLast()

        remPrev: Node = self.__head
        for _ in range(1, index):
            remPrev: Node = remPrev.next  # type: ignore

        toRemove: Node = remPrev.next  # type: ignore
        remPrev.next = remPrev.next.next  # type: ignore
        self.__size -= 1
        return toRemove.value

    def isEmpty(self):
        """Return true if this list contains no elements"""

        return self.__size == 0

    def getSize(self):
        """Return the number of elements in this list"""

        return self.__size

    def __str__(self):
        stringified: str = "["

        if self.__size == 0:
            return stringified + "]"

        current: Node = self.__head  # type: ignore
        for _ in range(self.__size):
            stringified += str(current.value)

            if current.next is not None:
                stringified += ", "
            else:
                stringified += "]"
                break

            current: Node = current.next

        return stringified

    def clear(self):
        """Remove all of the elements from this list"""

        self.__head = self.__tail = None
        self.__size = 0

    def contains(self, value) -> bool:
        """Return true if this list contains the specified element

        Arguments:
            value: The element to search for
        """

        for elem in self:
            if elem == value:
                return True

        return False

    def remove(self, value) -> bool:
        """Remove the first occurrence of the specified element from this list, if it is present.

        Arguments:
            value: The element to be removed
        """

        index: int = 0
        current: Node = self.__head  # type: ignore
        for _ in range(self.__size):
            if current.value == value:
                self.removeAt(index)
                return True

            current: Node = current.next  # type: ignore
            index += 1

        return False

    def get(self, index: int) -> Any:
        """Return the element at the specified position in this list.

        Arguments:
            index: The index of the element to return
        """

        for count, elem in enumerate(self):
            if count == index:
                return elem

        return None

    def indexOf(self, value: Any) -> int:
        """Get the index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element.

        Arguments:
            value: The element to search for
        """

        for count, elem in enumerate(self):
            if elem == value:
                return count

        return -1

    def lastIndexOf(self, value: Any) -> int:
        """Get the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element.

        Arguments:
            value: The element to search for
        """
        for count, elem in reversed(list(enumerate(self))):
            if elem == value:
                return count

        return -1

    def set(self, index: int, value: Any) -> None:
        """Set the element at the specified position in this list.

        Arguments:
            index: The index of the element to set
            value: The new value of the element
        """

        if index < 0 or index >= self.__size:
            return

        current: Node = self.__head  # type: ignore
        for i in range(index):
            if i == index:
                current.value = value
                break
            current = current.next  # type: ignore

    def __getitem__(self, index):
        return self.get(index)

    def __iter__(self):
        if self.__size == 0 or self.__head is None:
            raise StopIteration

        current: Node = self.__head
        for _ in range(self.__size):
            yield current.value
            current: Node = current.next  # type: ignore
