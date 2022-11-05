def maxGroupSize(arr, N, k):
        ans = [0 for i in range(k)]
        for i in arr:
            ans[i % k] += 1
        i = 1
        j = k - 1
        result = 0 if ans[0] == 0 else 1
        while i <= j:
            if i == j and ans[i]!=0:
                result+=1
                break
            result += max(ans[i], ans[j])
            i, j = i+1, j-1
        return result
