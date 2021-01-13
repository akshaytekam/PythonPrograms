"""
   * author - Akshay Tekam
   * date - 12/01/2021
   * time - 22:34:15
   * package - time
   * Title -  a Stopwatch Program for
   measuring the time that elapses between
   the start and end clicks
"""
import time

class Stopwatch:
    # this function returns the current system time in ticks
    def measureTime(self):
        print("start time")
        start_time = time.time()      # Start time
        stopper = input("Press enter to stop...")
        end_time = time.time()        # end time
        print("finished")

        print("-----------")
        duration = int(end_time - start_time)        # total duration between start and end
        print("It is:" + str(duration) + " seconds")

obj=Stopwatch()        # creating the object of class
obj.measureTime()      # calling the function using object