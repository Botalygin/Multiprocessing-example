import threading
import datetime

Flag = 0


class MyThread (threading.Thread):
   def __init__(self, name, counter):
       threading.Thread.__init__(self)
       self.threadID = counter
       self.name = name
       self.counter = counter

   def run(self):
       print("Starting " + self.name)

       threadLock.acquire()
       print_date(self.name, self.counter)

       threadLock.release()
       print("Exiting " + self.name)


def print_date(threadName, counter):
   datefields = []
   today = datetime.date.today()
   datefields.append(today)
   print(
      "%s[%d]: %s" % (threadName, counter, datefields[0])
   )


threadLock = threading.Lock()
threads = []

thread1 = MyThread("Thread", 1)
thread2 = MyThread("Thread", 2)
thread3 = MyThread("Thread", 3)

thread1.start()
thread2.start()
thread3.start()

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

for t in threads:
   t.join()

print("Exiting the Program!!!")