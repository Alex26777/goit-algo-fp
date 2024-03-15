class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current_node = dummy

    while list1 and list2:
        if list1.value < list2.value:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        
        current_node = current_node.next

    current_node.next = list1 or list2

    return dummy.next

# Приклад використання:
# Створення списку 1 -> 2 -> 4
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

# Створення списку 1 -> 3 -> 4
head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)

# Об'єднання відсортованих списків
merged_head = merge_sorted_lists(head1, head2)
# Виведення результату
while merged_head:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next
