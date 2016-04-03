import heapq
class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))#插入项为三元组，最后一项为实际push项，前两项为优先级
        self._index+=1#用于当优先级相同时按输入顺序排列。
    def pop(self):
        return heapq.heappop(self._queue)[-1]#实际输出只输出item项

if __name__=="__main__":
     q=PriorityQueue()
     q.push("ad",1)
     q.push("ab",2)
     q.push("ac",1)
     print(q.pop())
     print(q.pop())
     print(q.pop())