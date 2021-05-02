from django_clickhouse import migrations
from celery_app.clickhouse_models import TotalBalance


class Migration(migrations.Migration):
    operations = [
        migrations.CreateTable(TotalBalance)
    ]