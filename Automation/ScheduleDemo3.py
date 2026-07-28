import schedule
import time
import datetime


def Display():

    print("Jay ganesh...",datetime.datetime.now())
    
def main():

    print("Automation Started:")

    schedule.every(1).minute.do(Display)

    while True:

        schedule.run_pending()
        time.sleep(1)

    print("End od Automation")    
    

if __name__=="__main__":
    main()
