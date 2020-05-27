from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in memo:
                return [i, memo[tmp]]
            else:
                memo[num] = i

# from queue import Queue
from multiprocessing import Process, Queue
from datetime import datetime
import time


def write(q: Queue):
    while True:
        q.put(datetime.now())
        time.sleep(1)


def read(q: Queue):
    while True:
        print(q.get())
        time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=write, args=(q, ))
    p2 = Process(target=read, args=(q, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()