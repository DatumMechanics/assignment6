import random
from heap import Heap  # Assumes your code is saved as heap.py


def main():
    n = 16
    m = 16

    # Seed the random number generator for reproducible results
    random.seed(42)

    vals = [0] * (n + m)
    ordered = [0] * (n + m)

    # Create the heap data structure
    heap = Heap()
    print("== Inserting some into Heap")
    for i in range(n):
        vals[i] = random.randint(0, 63)
        heap.insert(vals[i], vals[i])

    # Copy the first n elements and sort them in descending order
    ordered[0:n] = vals[0:n]
    ordered[0:n] = sorted(ordered[0:n], reverse=True)

    # Examine and remove half of the values currently in the heap
    k = 0
    print("\n== Removing some from Heap: first / removed / priority (expected)")
    while k < n // 2:
        p = heap.max_priority()
        first = heap.max()
        removed = heap.max_dequeue()

        p_str = f"{p:4d}" if p is not None else "None"
        if first is not None and removed is not None:
            print(f"  - {first:4d} / {removed:4d} / {p_str} ({ordered[k]:4d})")
        else:
            print(f"  - (NULL) / (NULL) / {p_str} ({ordered[k]:4d})")
        k += 1

    # Add a second set of random integer values
    print("\n== Inserting more into Heap")
    for i in range(n, n + m):
        vals[i] = random.randint(0, 63)
        heap.insert(vals[i], vals[i])

    # Copy the remaining elements and sort the unexamined portion descending
    ordered[n : n + m] = vals[n : n + m]
    ordered[k : n + m] = sorted(ordered[k : n + m], reverse=True)

    # Remove all remaining elements from the heap
    print(
        "\n== Removing remaining from Heap: first / removed / priority (expected)"
    )
    while k < n + m:
        p = heap.max_priority()
        first = heap.max()
        removed = heap.max_dequeue()

        p_str = f"{p:4d}" if p is not None else "None"
        if first is not None and removed is not None:
            print(f"  - {first:4d} / {removed:4d} / {p_str} ({ordered[k]:4d})")
        else:
            print(f"  - (NULL) / (NULL) / {p_str} ({ordered[k]:4d})")
        k += 1

    # Check emptiness (prints 1 for True, 0 for False)
    is_empty_flag = 1 if heap.is_empty() else 0
    print(f"\n== Is Heap empty (expect 1)? {is_empty_flag}")

    # Explicitly clear heap references
    del heap


if __name__ == "__main__":
    main()
