"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
from heapq import heappush, heappop, heapify
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.upper, self.lower,self.k=  nums[:k-1], [], self.k
        heapify(self.upper)
        for i, num in enumerate(nums[k-1:]):
            if num <= self.upper[0]:
                heappush(self.lower, -num)
            else:
                heappush(self.upper, nums[i + k - 1])
                heappush(self.lower, -heappop(self.upper))

    def add(self, num: int) -> int:
        if self.k > 1 and num <= self.upper[0]:
            heappush(self.lower, -num)
        else:
            heappush(self.upper, num)
            heappush(self.lower, -heappop(self.upper))
        return -1 * self.lower[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)