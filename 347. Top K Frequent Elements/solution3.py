import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        unique = list(count.keys())
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            
            unique[right], unique[store_index] = unique[store_index], unique[right]
            
            return store_index
        
        def quickSelect(left, right, k_smallest) -> None:
            if left == right:
                return 
            
            pivot_index = partition(left, right, random.randint(left, right))
            if k_smallest == pivot_index:
                return
            elif k_smallest < pivot_index:
                 quickSelect(left, pivot_index - 1, k_smallest)
            else:
                 quickSelect(pivot_index + 1, right, k_smallest)
        
        
        n = len(unique)
        quickSelect(0, n - 1, n - k)
        return unique[n - k:]