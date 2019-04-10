from queue import Queue
from threading import Thread

NUM_CONSUMERS = 4

from datetime import datetime
startTime = datetime.now()

def next_num(num):
    prod = 1
    for i in str(num):
        prod *= int(i)
    return prod

def persistence(num,depth=0):
    if len(str(num)) == 1:
        return depth
    else:
        return persistence(next_num(num),depth=depth+1)

def for_persistence(num):
    depth = 0
    while len(str(num))>1:
        num = next_num(num)
        depth += 1
    return depth

#numbers must start with either one two or one three but not both
#only one 4 or one 6 but not both

#numbers start with either {{}, {2}, {3}, {4}, {6}, {2,6}, {3,5}, {5, 5,...}}
# we will ignore 5s.
def produce(q,prefix):
    length = 4 
    while True:
        for n7 in reversed(range(length-len(prefix)+1)):
            for n8 in reversed(range(length-len(prefix)-n7+1)):
                n9 = length - len(prefix)-n7-n8
                num = int(prefix+"7"*n7+"8"*n8+"9"*n9)
                q.put(num)
        length += 1
        if length >100:
            break
        #print(prefix,length, datetime.now() - startTime, q.qsize())

def consume(q):
    while not q.empty():
        num = q.get()
        q.task_done()
        p = for_persistence(num)
        if p > 4:
            print(p,num,q.qsize())

if __name__ == "__main__":
    qs = []
    for prefix in ["2","26","3","4","6",""]:
        q = Queue()
        qs.append(q)
        p = Thread(target=produce, args=(q,prefix))
        p.start()
    consumers = []
    for q in qs:
        for i in range(NUM_CONSUMERS):
            c = Thread(target=consume,args=(q,))
            c.start()
            consumers.append(c)
    for q in qs:
        q.join()




