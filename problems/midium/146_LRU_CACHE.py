class DoubleLinkedList:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            node = DoubleLinkedList(key=key, value=value)
            self.add_to_head(node)
            self.dict[key] = node
            self._size += 1

            if self._size > self.capacity:
                deleted_node = self.remove_from_tail()
                self.dict.pop(deleted_node.key)
                self._size -= 1
        else:
            node = self.dict[key]
            node.value = value
            self.move_to_head(node)

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_from_tail(self):
        node = self.tail.prev
        self.remove_node(node)

        return node


if __name__ == '__main__':
    capacity = 2
    obj = LRUCache(capacity)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))
    obj.put(3, 3)
    print(obj.get(2))
    obj.put(4, 4)
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))


