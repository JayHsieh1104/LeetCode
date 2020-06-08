class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ret = []
        people.sort(key = lambda x: (-x[0], x[1]))
        
        for p in people:
            ret.insert(p[1], p)
            
        return ret