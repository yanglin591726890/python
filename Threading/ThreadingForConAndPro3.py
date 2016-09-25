from threading import BoundedSemaphore,Lock,Thread
from atexit import register
from time import sleep,ctime
from random import randrange

MAX = 5 
candytray = BoundedSemaphore(MAX)
lock = Lock()

def refill():
	lock.acquire()
	print('refilling candy....')
	try:
		candytray.release()
	except ValueError :
		print('full,skipping')
	else:
		print('refill one')
	lock.release()

def buy():
	lock.acquire()
	print('buying candy....')
	if candytray.acquire(False):
		print('Buy one')
	else:
		print('empty,skinping')
	lock.release()

def producer(loops):
	for i in range(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	for x in range(loops):
		buy()
		sleep(randrange(3))

def main():
	print('starting at :',ctime())
	nloops = randrange(2,6)
	print("the candy full with %s"%MAX)

	Thread(target=producer,args=(randrange(nloops,nloops+MAX+2),)).start()
	Thread(target = consumer,args = (randrange(nloops,nloops+MAX+2),)).start()

@register
def _atexit():
	print("all done at :",ctime())

if __name__ == '__main__':
	main()

	
