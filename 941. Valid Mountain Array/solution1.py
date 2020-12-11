class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        
        is_going_up = True
        
        for i in range(1, len(arr)-1):
            if is_going_up:
                if arr[i] < arr[i+1]:
                    continue
                elif arr[i] > arr[i+1]:
                    is_going_up = False
                else:
                    return False
            else:
                if arr[i] <= arr[i+1]:
                    return False
        
        return is_going_up == False