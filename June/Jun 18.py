class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d={}
        l=len(arr)
        for i in range(l):
            if arr[i] in d.keys():
                d[arr[i]].append(i)
            else:
                d[arr[i]]=[i]
        
        #breadth first search
        q=deque([0])
        steps=-1
        #print(d)
        visited=[0 for i in range(l)]
        visited[0]=1
        while q:
            size=len(q)
            steps+=1
            #print('q=',q)
            for i in range(size):
                index=q.popleft()
                if index==l-1:
                    return steps

                adds=[index-1,index+1]
                if arr[index] in d.keys():
                    adds+=d[arr[index]]
                    del d[arr[index]]
                for add in adds:
                    if add>=0 and add<l and visited[add]==0:
                        q.append(add)
                        visited[add]=1
                
                
        
        return 0
