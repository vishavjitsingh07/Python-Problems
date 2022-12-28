class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0
        c = Counter(s)
        if c["a"]<k or c["b"]<k or c["c"]<k: return -1
        n = len(s)
        da = defaultdict()
        db = defaultdict()
        dc = defaultdict()
        da[0] = db[0] = dc[0] = n
        aCount = bCount = cCount = 0
        for i in range(n-1, -1, -1):
            if s[i] == "a":
                aCount += 1
                da[aCount] = i
            if s[i] == "b":
                bCount +=1
                db[bCount] = i
            if s[i] == "c":
                cCount +=1
                dc[cCount] = i
                
        aCount = bCount = cCount = 0
        ans = n - min(da[k], db[k], dc[k])
        for i in range(n):
            if s[i] == "a": aCount +=1
            if s[i] == "b": bCount +=1
            if s[i] == "c": cCount +=1
            aC = max(k- aCount, 0)
            bC = max(k- bCount, 0)
            cC = max(k- cCount, 0)
            ans = min(ans, n - min(da[aC], db[bC], dc[cC]) + i + 1)
        return ans
            
