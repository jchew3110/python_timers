import time
def countdown(n):
    while n>0:
        print(n)
        time.sleep(1)
        n-=1
        if n==0:
            print('DONE')
countdown(20)
