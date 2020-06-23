class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        
        for j in range(1, len(rating)-1):
            counter_left_less_than_j = 0
            counter_right_less_than_j = 0
            counter_left_greater_than_j = 0
            counter_right_greater_than_j = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    counter_left_less_than_j += 1
                elif rating[i] > rating[j]:
                    counter_left_greater_than_j += 1
            for k in range(j+1, len(rating)):
                if rating[j] < rating[k]:
                    counter_right_greater_than_j += 1
                elif rating[j] > rating[k]:
                    counter_right_less_than_j += 1    
            counter += counter_left_less_than_j * counter_right_greater_than_j + counter_left_greater_than_j * counter_right_less_than_j
                   
        return counter