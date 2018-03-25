# -*- coding: utf-8 -*-
import multiprocessing
import time
import robot,Main

def add():
    print("Add Başladı")
    while True:
        print (1)
        time.sleep(1)

def sud():
     print("Sud Başladı")
     while True:
        print(0)
        time.sleep(3)

if __name__ == '__main__':

    # p1 = multiprocessing.Process(name='Add', target=robot.autoMode)

    Main.go()
    print 'thread satrını geldi.'
    p2 = multiprocessing.Process(name='Sud', target=robot.souffleMode_threaded(""))




    # join() main programa geri verir dataları.
    # gives us the total running time -> time.time()-t

