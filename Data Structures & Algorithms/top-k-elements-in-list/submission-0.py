import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_elem = {}

        for n in nums:
            count_elem[n] = count_elem.get(n, 0) + 1
        
        heap = []
        for num, freq in count_elem.items():
            heapq.heappush(heap, (-freq, num))

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
        return result