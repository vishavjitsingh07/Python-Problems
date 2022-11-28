class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = set()
        lost1 = set()
        lost2 = set()
        for win, loss in matches:
            if win not in lost1 and win not in lost2:
                winner.add(win)
            if loss not in lost1 and loss not in lost2:
                if loss in winner:
                    winner.remove(loss)
                lost1.add(loss)
            elif loss in lost1:
                lost1.remove(loss)
                lost2.add(loss)
        return [sorted(list(winner)), sorted(list(lost1))]

