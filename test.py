from threading import *
import time
s=Semaphore(3)
def wish(name):
	s.acquire()
	for i in range(5):
		print('Good Morning:',end='')
		time.sleep(3)
		print(name)
	s.release()
t1=Thread(target=wish,args=('Raj',))
t2=Thread(target=wish,args=('Muni',))
t3=Thread(target=wish,args=('Seemala',))
t1.start()
t2.start()
t3.start()

