from main.celery import app
from .services import balance, control_balance


@app.task
def all_balance():
    balance()


@app.task
def check_balance(client_id):
    control_balance(client_id)