# when using threads, it's like you're running multiple programs at once
# thread - a block of code that executes

import threading
import time
import random


def execute_thread(i):
    print("thread {} sleeps at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep_time = random.randint(1, 5)
    time.sleep(rand_sleep_time)
    print("thread {} stops sleeping at {}".format(i, time.strftime("%H:%M:%S", time.gmtime())))


for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()
    print("active threads:", threading.active_count())
    print("thread objects:", threading.enumerate())


# can also subclass threads
class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        get_time(self.name)
        print("thread", self.name, "execution ends")


def get_time(name):
    print("thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    rand_sleep = random.randint(1, 5)
    time.sleep(rand_sleep)


thread1 = CustThread("1")
thread2 = CustThread("2")

thread1.start()
thread2.start()

print("thread 1 alive:", thread1.is_alive())
print("thread 2 alive", thread2.is_alive())

print("thread 1 name:", thread1.getName())
print("thread 2 name:", thread2.getName())

thread1.join()
thread2.join()

print("execution ended")


# using synchronizing threads to simulate a bank account:
class BankAccount(threading.Thread):
    acct_balance = 100

    def __init__(self, name, money_request):
        threading.Thread.__init__(self)
        self.name = name
        self.money_request = money_request

    def run(self):
        thread_lock.acquire()
        BankAccount.get_money(self)
        thread_lock.release()

    @staticmethod
    def get_money(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name, customer.money_request, time.strftime("%H:%M:%S", time.gmtime())))
        if BankAccount.acct_balance - customer.money_request > 0:
            BankAccount.acct_balance -= customer.money_request
            print("new account balance: $", BankAccount.acct_balance)
        else:
            print("not enough money in account")
            print("account balance is: $", BankAccount.acct_balance)

        time.sleep(3)


thread_lock = threading.Lock()
doug = BankAccount("doug", 1)
paul = BankAccount("paul", 100)
sally = BankAccount("sally", 50)

doug.start()
paul.start()
sally.start()

doug.join()
paul.join()
sally.join()

print("execution ends")
