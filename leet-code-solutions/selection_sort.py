from typing import List

class Solution:
    """
        Class that perform the selection sort algorithm on unsorted array of integers.
        Time Complexity: O(N^2)
        Space Complexity: O(1)
    """
    def select(self, arr: List[int], i: int) -> int:
        min_index = i
        for j in range (min_index+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        return min_index
    
    def selectionSort(self, arr: List[int], i: int) -> List[int]:
        for i in range(len(arr)):
            min_index = self.select(arr, i)
            # Swap the elements of the array using the min index with the current index.
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


if __name__ == "__main__":
    c = Solution()
    my_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(c.selectionSort(my_array.copy(), 0))
