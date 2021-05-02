from django.http import HttpResponse
from .tasks import check_balance


def check_new_operation(request):

    if request.method == 'GET':
        client_id = request.GET['client_id']
        check_balance.delay(client_id)  # run task
        return HttpResponse('200 OK')