class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        
        for num in nums:

            if num not in count:
                 count[num] = count.get(num, 0)

            count[num] += 1
        
        for i in range(k):
           num = max(count, key=count.get)
           result.append(num)
           count.pop(num)


        return result