class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x = bisect_right(letters, target)
        return letters[0 if x >= len(letters) else x]
