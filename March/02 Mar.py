  #https://practice.geeksforgeeks.org/problems/jumping-numbers3805/1  
  def jumpingNums(self, X):
        if X<=10: return X
        s = set(list(range(1, 13)))
        def dfs(i):
            if i>=X: return
            
            newNum = i%10
            if 0<= newNum < 9:
                new = i*10 + newNum+1
                if new<= X:
                    s.add(new)
                    dfs(new)
                    
            if 9>=newNum > 0:
                new = i*10 + newNum-1
                if new<= X:
                    s.add(new)
                    dfs(new)
                    
            return s
        
        for i in range(1, 11):
            dfs(i)
            
        return max(s)
