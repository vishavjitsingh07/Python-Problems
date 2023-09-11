class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        hashmap = defaultdict(list)

        for i,n in enumerate(groupSizes):
            hashmap[n].append(i)
        
        res = []

        for v,arr in hashmap.items():
            temp = []
            for i in arr:
                if len(temp)<v:
                    temp.append(i)
                if len(temp)==v:
                    res.append(temp)
                    temp = []
        return res
        
