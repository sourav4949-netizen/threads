"""when we are not creating any thread and only usong a main function then it is called as single threading
To improve the performance of our applications and to better utilise the processor we can use threading in our application

3 ways to do it
-- using a function
t=Thread(target=functtonName,args)
t.start()

-- extending the thread class for
override the run() method to
class MyThread(Thread)
override the run()
t.start()

--without extending the thread class
class MyThread
display()
t=Thraed(target=myobj.display(),args)
"""