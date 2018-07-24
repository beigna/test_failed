import dramatiq

from .models import ModelB


@dramatiq.actor
def create_model_b():
    ModelB.objects.create(model_id=1, value="1")
