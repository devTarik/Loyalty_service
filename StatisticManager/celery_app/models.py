from django_clickhouse.models import ClickHouseSyncModel
from django.db import models


class Balance(ClickHouseSyncModel):

    balance = models.IntegerField(max_length=50)
    datetime = models.DateTimeField()
    

