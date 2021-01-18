class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mDict = collections.defaultdict(list)
        
        for path in paths:
            path = path.split(" ")
            for i in range(1, len(path)):
                root_path = path[0]
                sub_path = path[i].split("(")[0]
                content = path[i].split("(")[1][:-1]   
                mDict[content].append(root_path + "/" + sub_path)
        
        res = []
        for (key, values) in mDict.items():
            if len(values) > 1:
                res.append(values)
        
        return res