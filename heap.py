class HeapElement:
    """Represents an individual node inside the heap."""
    def __init__(self, data, priority: int):
        self.data = data
        self.priority = priority


class Heap:
    """Represents the max-heap data structure."""
    def __init__(self):
        """
        Initializes an empty heap.
        """
        pass

    def __del__(self):
        """
        Clears heap references if explicit cleanup is needed.
        """
        pass

    def is_empty(self) -> bool:
        """
        Returns True if the heap contains no elements, False otherwise.
        """
        pass

    def insert(self, data, priority: int) -> None:
        """
        Inserts data with a given priority and restores the heap property.
        """
        pass

    def max(self):
        """
        Returns the data of the root element without removing it.
        """
        pass

    def max_priority(self) -> int:
        """
        Returns the priority value of the root element.
        """
        pass

    def max_dequeue(self):
        """
        Extracts and returns the data of the root element, then restores the heap property.
        """
        pass

    def _percolate_up(self, index: int) -> None:
        """Moves an element up the tree until it satisfies the max-heap property."""
        pass

    def _percolate_down(self, index: int) -> None:
        """Moves an element down the tree until it satisfies the max-heap property."""
        pass
