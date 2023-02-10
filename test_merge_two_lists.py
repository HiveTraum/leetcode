from dataclasses import dataclass
from typing import Optional

import pytest


@dataclass
class ListNode:
    val: int = 0
    next: Optional['ListNode'] = None


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        current = first = ListNode()

        while True:
            if list1 is None and list2 is None:
                break
            elif (list1 is not None and list2 is not None and list1.val > list2.val) or list1 is None:
                current.next = list2
                list2 = list2.next
                current = current.next
            else:
                current.next = list1
                list1 = list1.next
                current = current.next

        return first.next


solution = Solution()

cases = (
    (ListNode(val=0), ListNode(val=1), [0, 1]),
    (ListNode(val=0), None, [0]),
    (None, ListNode(val=0), [0]),
)


def traverse(node: ListNode) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next

    return result


@pytest.mark.parametrize(("list1", "list2", "expected"), cases)
def test_merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode], expected: Optional[ListNode]):
    assert traverse(solution.mergeTwoLists(list1, list2)) == expected


if __name__ == '__main__':
    for _list1, _list2, _ in cases:
        solution.mergeTwoLists(_list1, _list2)
