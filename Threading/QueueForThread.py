from Queue import Queue
from time import ctime,sleep
from threading import Thread
from random import randint

def writeQ(queue):
	print 'product:'
	queue.put('xxx',True)
	print 'size now ',queue.qsize()

def readQ(queue):
	print 'consummer:'
	value = queue.get()
	print "size now ",queue.qsize()

def productor(queue,loops):
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1,3))

def consummer(queue,loops):
	for i in range(loops):
		readQ(queue)
		sleep(randint(1,3))

def main():
	q = Queue(32)
	print "starting at ",ctime()
	t1 = Thread(target=productor,args = (q,randint(4,6),))
	t2 = Thread(target=consummer,args = (q,randint(4,6),))

	for i in [t1,t2]:
		i.start()

	t1.join()
	t2.join()
	print 'all done'

if __name__ == '__main__':
	main()
