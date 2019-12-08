import unittest
import heapq
from typing import List
from collections import defaultdict


def highFive(self, items: List[List[int]]) -> List[List[int]]:
        heaps = collections.defaultdict(list)

        for scorer, score in items:
            heapq.heappush(heaps[scorer], score)

            if len(heaps[scorer]) > 5: 
                heapq.heappop(heaps[scorer])

        print(heaps)
        return [[i, sum(heaps[i]) // len(heaps[i])] for i in sorted(heaps)]
