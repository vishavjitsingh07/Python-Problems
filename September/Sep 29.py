class Solution:
    def setSetBit(self, x, y, l, r):
        x1=x//(2**(l-1))
        y1=y//(2**(l-1))
        for i in range(l,r+1):
            if y1%2==1 and x1%2==0:
                x+=(2**(i-1))
            y1//=2
            x1//=2
        return x
