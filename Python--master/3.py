from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(2)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()
#t1.run()
#t2.run()

t1.start()
#sleep(0.2)
t2.start()

#t1.join()
print('t1 tread complited')
#t2.join()
print('t2 tread complited')

print("Bye")