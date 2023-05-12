def mostPoints(self, questions: List[List[int]]) -> int:
        
        def getPoints(idx: int) -> int:
            if idx >= len(questions):
                return 0
            if idx not in idx_to_points:
                points, brain = questions[idx]
                cur = points + getPoints(idx + brain + 1) 
                idx_to_points[idx] = max(cur, getPoints(idx + 1))
            return idx_to_points[idx]
        
        idx_to_points = {}
        return getPoints(0)
