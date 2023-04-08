class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        clone = {}
        visited = set()

        def generate(node):
            queue = collections.deque()
            queue.append(node)
            while queue:
                curr = queue.popleft() 
                if curr not in clone: clone[curr] = Node(curr.val)
                if curr in visited:continue

                visited.add(curr)
                for neighb in curr.neighbors:
                    if neighb not in clone: clone[neighb] = Node(neighb.val)

                    clone[curr].neighbors.append(clone[neighb])
                    queue.append(neighb)
        generate(node)
        return clone[node]
