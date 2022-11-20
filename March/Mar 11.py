class Solution:
    def calculate(self, s: str) -> int:
        stck = []
        stckP = []
        i = 0
        n = len(s)
        lenS = 0
        while i < n:
            if s[i] == '(':
                stckP.append(lenS)
                stck.append(s[i])
                i += 1
                lenS+=1
                
            elif s[i] == ')':
                lastB = stckP[-1]
                equation = "".join(stck[lastB:lenS+1]) + ")"
                ans = str(eval(equation))
                while lenS>stckP[-1]:
                    stck.pop()
                    lenS-=1
                stckP.pop()
                stck.append(ans)
                i+=1
                lenS+=1
                
            else:
                stck.append(s[i])
                i += 1
                lenS+=1
                
        return eval("".join(stck))

