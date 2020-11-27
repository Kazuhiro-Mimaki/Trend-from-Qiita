from apscheduler.schedulers.blocking import BlockingScheduler
import twitter

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=9)
def scheduled_job():
    tweitter.post()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=20)
def scheduled_job():
    tweitter.post()

sched.start()