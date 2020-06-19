class Solution:
    def hIndex(self, citations: List[int]) -> int:      
        lo = 0
        hi = len(citations) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] < len(citations) - mid:
                lo = mid + 1
            elif citations[mid] > len(citations) - mid:
                hi = mid - 1
            else:
                return len(citations) - mid
        
        return len(citations) - lo