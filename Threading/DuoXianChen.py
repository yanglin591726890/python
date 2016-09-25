from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen as uopen

REGEX = compile('#([\d,]+) in books')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
	"126548":"Core Python Programming"
}

def getRanking(isbn):
	with uopen('{0}{1}'.format(AMZN,isbn)) as page:
		return str(REGEX.findall(page.read())[0],'utf-8')

def main():
	print("at:",ctime(),"on Amazon...")
	with ThreadPoolExecutor(3) as executor :
		for isbn ranking in zip(ISBNs,executor.map(getRanking,ISBNs)):
			print "--%r ranked %s " % (ISBNs[isbn],ranking)
	print "all done "

if __name__ == '__main__':
	main()