#-*- coding:utf8 -*- 

import multiprocessing
import time
import subprocess

def f():
    subprocess.call("git pull", shell=True)

def work():
   while 1:
       f()
       time.sleep(10)

if __name__ == '__main__':
    p = multiprocessing.Process(target=work,)
    p.start()
    p.deamon = True
    #while 1:
    #    print '这是主进程,每1秒执行一次'
    #    subprocess.call("git pull", shell=True)
    #    time.sleep(1)
