import pytest
from django.test import Client
import json

from myapp.models import ModelA, ModelB


@pytest.mark.django_db
def test_optout(broker, worker):
    c = Client()
    url = '/test/'

    data = {
        'some': 'value',
    }

    # DB Fixtures
    ModelA.objects.create(name='Pepe', size=256)
    # ----------;

    res = c.post(url, json.dumps(data), 'application/json')
    assert res.status_code == 200

    # Procesar tareas encoladas
    broker.join("default")
    worker.join()

    ma = ModelA.objects.get(name='Pepe')
    assert ma.size == 256

    mb = ModelB.objects.get(pk=1)
    assert mb.model == ma
