from django.http import HttpResponse

from .tasks import create_model_b

# Create your views here.


def test_view(request):
    create_model_b.send()
    # create_model_b()  # <<< This works!
    return HttpResponse('Hi!')
