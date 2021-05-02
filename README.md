___
### **PointManager** app for accumulation of points for the loyalty program
___

### **StatisticManager** Celery application for collect statistics and save to ClickHouse databases
___

## RUN

* PointManager run to port **8000**
* StatisticManager run to port **8081**

* ClickHouse need have database **"statistics_db"**

* Celery Worker need run on the root dir **StatisticsManager** with command  
`celery -A main worker -l info`

* Celery Beat need run on the root dir **StatisticsManager** with command
`celery -A main beat -l info`



