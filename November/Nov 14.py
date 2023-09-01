class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        arr = [0, 1]
        count = 2
        pow2 = 0
        while count<=n:
            if (count)&(count-1) == 0 :
                arr.append(1)
                pow2 +=1
            else:
                arr.append(arr[count-2**pow2]+1)
            count+=1
        return arr
