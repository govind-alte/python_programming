import schedule
import time
import datetime


def Display():
    print("Jay ganesh...",datetime.datetime.now())
def main():
    print("Automation Started:")

    schedule.every(1).minute.do(Display)
    

if __name__=="__main__":
    main()
