import heapq

N = int(input())
heap = []

for _ in range(N):
     number = int(input())
     if number == 0:
         if heap:
             print(heapq.heappop(heap))
         else:
             print(0)
     else:
         heapq.heappush(heap, number)
