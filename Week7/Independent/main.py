"""Sorting algorithms"""
from datetime import timedelta
from random import randint
from sys import setrecursionlimit
from threading import Thread
from timeit import timeit
from typing import Any, Callable

ONE_THOUSAND: int = 1000

SortList = list[int]


def selectionSort(toSort: SortList) -> None:
    """Selection sort

    WARNING
        This function applies the changes to the original array.
    """

    for i, elem in enumerate(toSort):
        minIndex = i

        for j in range(i + 1, len(toSort)):
            if toSort[j] < toSort[minIndex]:
                minIndex = j

        toSort[i], toSort[minIndex] = toSort[minIndex], elem


def bubbleSort(toSort: SortList) -> None:
    """Bubble sort

    WARNING
        This function applies the changes to the original array.
    """
    reqNextPass: bool = True

    k: int = 1
    while k < len(toSort) and reqNextPass:
        reqNextPass = False

        for i in range(len(toSort) - k):
            if toSort[i] > toSort[i + 1]:
                toSort[i], toSort[i + 1] = toSort[i + 1], toSort[i]
                reqNextPass = True

        k += 1


def mergeSort(toSort: SortList) -> SortList:
    """Merge sort"""

    def merge(left: SortList, right: SortList) -> SortList:
        """Merge two sorted lists"""

        merged: SortList = []
        leftIndex: int = 0
        rightIndex: int = 0

        # Add both lists to another list until one or both of them is exhausted.
        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] < right[rightIndex]:
                merged.append(left[leftIndex])
                leftIndex += 1
            else:
                merged.append(right[rightIndex])
                rightIndex += 1

        # Add the rest of the lists if there is any.
        merged += left[leftIndex:]
        merged += right[rightIndex:]

        return merged

    if not len(toSort) > 1:
        return toSort

    # Merge sort the left and right half of the list.
    return merge(
        mergeSort(toSort[: len(toSort) // 2]),
        mergeSort(toSort[len(toSort) // 2 :]),
    )


def quickSort(toSort: SortList, lowerBound: int = ..., upperBound: int = ...) -> None:
    """Quick sort

    WARNING
        This function applies the changes to the original array.
    """

    if lowerBound is ... or upperBound is ...:
        lowerBound, upperBound = 0, len(toSort) - 1

    # If the condition is not fullfilled that means that the
    # list is already partitioned as much as possible.
    if lowerBound < upperBound:
        pivot = toSort[upperBound]

        # The variable keeps track of the index of the greatest element
        greaterIndex = lowerBound - 1

        for i in range(lowerBound, upperBound):
            if toSort[i] <= pivot:
                # The greaterIndex works because we increase it only when we find a smaller element.
                # Since we have already checked that the elements before are greater,
                # we can simply just use one of the elements in the front of the list.
                # For example, the list 8 7 2 9 4 has the pivot 4.
                # We would loop to 2, and increase greaterIndex to 0.
                # This would give us 8 as a greaterIndex.
                greaterIndex = greaterIndex + 1
                toSort[greaterIndex], toSort[i] = toSort[i], toSort[greaterIndex]

        pivotIndex = greaterIndex + 1

        toSort[pivotIndex], toSort[upperBound] = (
            toSort[upperBound],
            toSort[pivotIndex],
        )

        quickSort(toSort, lowerBound, pivotIndex - 1)
        quickSort(toSort, pivotIndex + 1, upperBound)


def main() -> None:
    """Check times of all the sort methods"""

    def threadGen(
        func: Callable[[SortList], None | SortList],
        toSort: SortList,
        doPrint: bool,
        hasReturnVal: bool = False,
    ) -> Callable[[], Any]:
        """Wrapper for threads"""

        def wrapper() -> Any:
            """Wrapper for threads"""

            if hasReturnVal:
                sortedList = func(toSort)
            else:
                sortedList = toSort.copy()
                func(sortedList)

            if doPrint:
                print(
                    f"{func.__name__.capitalize().replace('sort', ' sorted')} list: {sortedList}"
                )

        return wrapper

    setrecursionlimit(2000)

    length, inThousands, viewSorted, viewUnsorted = (
        int(input("Enter the length of the list: ")),
        bool(int(input("Multiply that by 1,000? (1/0): "))),
        bool(int(input("Do you want to view the sorted list? (1/0): "))),
        bool(int(input("Do you want to view the unsorted list? (1/0): "))),
    )

    toSort: SortList = [
        randint(0, 100) for _ in range(length * ONE_THOUSAND if inThousands else length)
    ]

    if viewUnsorted:
        print("Unsorted:", toSort)

    # fmt: off
    # pylint: disable=line-too-long
    Thread(target=lambda: print("Selection Sort:", timedelta(seconds=timeit(threadGen(selectionSort, toSort, viewSorted), number=1)))).start()
    Thread(target=lambda: print("Bubble Sort:", timedelta(seconds=timeit(threadGen(bubbleSort, toSort, viewSorted), number=1)))).start()
    Thread(target=lambda: print("Merge Sort:", timedelta(seconds=timeit(threadGen(mergeSort, toSort, viewSorted, True), number=1)))).start()
    Thread(target=lambda: print("Quick Sort:", timedelta(seconds=timeit(threadGen(quickSort, toSort, viewSorted), number=1)))).start()
    # pylint: enable=line-too-long
    # fmt: on


if __name__ == "__main__":
    main()
