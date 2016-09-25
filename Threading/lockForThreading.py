from threading import Thread,Lock,currentThread
from random import randrange
from atexit import register
from time import ctime,sleep

class CleanOutputSet(set):
	def __str__(self):
		return ','.join(x for x in self)

remaining = CleanOutputSet()
lock = Lock()
loop = (randrange(2,5) for x in range(randrange(3,7)))
 

def loops(nesc):
	"""
		this is a way by use of lock
		acquire() get the lock 
		release() release the lock
	"""
	myName = currentThread().name
	lock.acquire()
	print('[%s] started %s ' % (ctime(),myName))
	remaining.add(myName)
	lock.release()
	sleep(nesc)
	lock.acquire()
	print('[%s ] ending %s '%(ctime(),myName))
	remaining.remove(myName)
	print('     (remaining:%s)'%(remaining or 'NONE'))
	lock.release()

def loopByWith(nesc):
	myName = currentThread().name
	with lock:
		print('[%s] started %s ' % (ctime(),myName))
		remaining.add(myName)
	sleep(nesc)
	with lock:
		print('[%s ] ending %s '%(ctime(),myName))
		remaining.remove(myName)
		print('     (remaining:%s)'%(remaining or 'NONE'))

	

def main():
	for nesc in loop:
		Thread(target=loopByWith,args=(nesc,)).start()

@register
def  _atexit():
	print('all Done at:',ctime())

if __name__ == '__main__':
	main()
