from django_clickhouse.clickhouse_models import ClickHouseModel
from infi.clickhouse_orm.engines import Log
from infi.clickhouse_orm import fields
from celery_app.models import Balance


class TotalBalance(ClickHouseModel):
    django_model = Balance
    
    sync_enabled = True
    
    balance = fields.UInt64Field()
    datetime = fields.DateTimeField()
    
    engine = Log()