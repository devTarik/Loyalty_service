### **PointManager** app for accumulation of points for the loyalty program
___
### **StatisticManager** Celery application for collect statistics and save to ClickHouse databases
___
## RUN

* PointManager run to port **8000**
* StatisticManager run to port **8081**

* In Postgres need create database **"point_manager"**
* In ClickHouse need create database **"statistics_db"**

* Celery Worker need run on the root dir **StatisticsManager** with command `celery -A main worker -l info`

* Celery Periodic Tasks need run on the root dir **StatisticsManager** with command `celery -A main beat -l info`
___
## Example request

> *Create user*
>> `http://localhost:8000/auth/users/  (POST)`

```json
{
  "email": "test@gmail.com",
  "username": "test_user",
  "password": "test123Pass",
}
```
___
> *Get Token*
>> `http://localhost:8000/auth/token/login (POST)`

```json
{
  "username": "test_user",
  "password": "test123Pass",
}
```
___
> *Create new client* 
>> `http://localhost:8000/api/v1/points/client/create (POST)`
>>> *example* `Headers {Authorization: "Token ..."}`

```json
{
  "name": "Client_1",
  "points": 0,
}
```
---
> *Get list all clients*
>> `http://localhost:8000/api/v1/points/client/list (GET)`
```
{}
```
___
> *Create new operation* 
>> `http://localhost:8000/api/v1/points/operations/create (POST)`

```jsonc
{
  "client": 1,   // id client
  "act": true,   // true = add points, false = subtract points
  "descript": "add 100 points",   // field may be missing 
  "points": 100,
}
```
___
> *Get list all operation* 
>> `http://localhost:8000/api/v1/points/operations/list (GET)`

```json
{}
```
___
