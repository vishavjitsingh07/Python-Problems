class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [val for val, _ in Counter(nums).most_common(k)]
