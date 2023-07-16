class Solution:
    def rev(self, queue):
        stack = []
    
        while not queue.empty(): stack.append(queue.get())
        while stack: reversed_queue.put(stack.pop())
    
        return reversed_queue
