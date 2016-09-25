#conding = utf-8

def countNumbers(filename,ss):
	"""
	@filename	jiushi file name
	@st			the char that you must find
	"""
	count = 0 

	for st in open(filename):
		count += st.count(ss)

	return count

def main():
	filename = raw_input("filename:")
	st = raw_input("char:")

	count = countNumbers(filename,st)
	print count

# import os
# from threading import Thread,currentThread,Lock
# from time import ctime
# lock = Lock()

# con = 0

# def read(filename,begin,length,sub):
# 	with open(filename) as f :
# 		f.seek(begin)
# 		data = f.read(length)
# 		count = data.count(sub)
# 	with lock:
# 		print currentThread().name,"count:",count
# 		global con
# 		con +=count



# def main():
# 	filename = raw_input("filename:")
# 	st = raw_input("char:")
# 	filesize = os.path.getsize(filename)

# 	threadNo = 3 
# 	n = int(filesize / threadNo)

# 	threads = []

# 	for seeks in  xrange(0,filesize,n):
# 		t = Thread(target = read,args=(filename,seeks,n-1,st,))
# 		threads.append(t)

# 	for i in threads:
# 		i.start()

# 	for i in threads:
# 		i.join()
# 	print con


if __name__ == '__main__':
	main()