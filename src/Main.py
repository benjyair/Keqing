from ViewModel import ViewModel
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": job start")
    vm = ViewModel()
    vm.connect()
    codes = ["000751",
             "005827",
             "162605",
             "001875",
             "260108",
             "008273",
             "050026",
             "001986",
             "001837",
             "050023",
             "163415",
             "968061",
             "110011",
             "000083",
             "110022",
             "005176",
             "161005",
             "163406",
             "040046",
             "519697"]
    vm.sync_favourite(codes)
    vm.sync_rank()
    vm.dispose()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": job end")


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', day_of_week='1-5', hour=9, minute=0)
    scheduler.add_job(job, 'cron', day_of_week='1-5', hour=23, minute=30)
    scheduler.start()
    job()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": scheduler start")

