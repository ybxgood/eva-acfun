from apscheduler.schedulers.background import BackgroundScheduler
from jobs.article import crawlNewArticleJob, crawlArticleDetailJob, completeDetailAndSaveJob
import time

import logging
logging.basicConfig(level=logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
scheduler = BackgroundScheduler()



# scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# crawlNewArticleJob()
# crawlArticleDetailJob()
scheduler.add_job(crawlNewArticleJob, name='crawlNewArticleJob', trigger='interval', minutes=10)
scheduler.add_job(crawlArticleDetailJob, name='crawlArticleDetailJob', trigger='cron', hour='10')
scheduler.add_job(completeDetailAndSaveJob, name='completeDetailAndSaveJob', trigger='interval', minutes=10)
scheduler.start()

while True:
  time.sleep(2)
