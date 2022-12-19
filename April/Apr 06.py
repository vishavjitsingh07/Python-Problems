#User function Template for python3
import collections
from typing import List
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, k : int) -> int:
        adj = collections.defaultdict(list)
        
        for u,v,w in flights:
            adj[u].append([v,w])
        
        costs = [-1 for i in range(n+1)]
        costs[k] = 0

        q = collections.deque()
        q.append([k,costs[k]])
    
        while(q):
            curNode = q.popleft()
            node=curNode[0]
            cost=curNode[1]
    
            for nextNode,nextCost in adj[node]:
                if(costs[nextNode]==-1):
                    costs[nextNode] = cost+nextCost
                    q.append([nextNode,costs[nextNode]])
                else:
                    if(costs[nextNode]>cost+nextCost):
                        costs[nextNode] = cost+nextCost
                        q.append([nextNode,costs[nextNode]])
        
        ans = 0
        for c in costs[1:]:
            if(c==-1):
                return -1
            ans = max(ans,c)
        
        return ans
        
