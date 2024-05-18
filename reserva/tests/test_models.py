from datetime import date

import pytest
from model_bakery import baker
from reserva.models import Reserva

@pytest.mark.django_db
def test_str_reserva_deve_retornar_string_formatada():
    data_reserva = date(2022, 8, 30)
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data_reserva,
        turno='tarde'
    )
    assert str(reserva) == 'Tom: 2022-08-30 - tarde'

def test_config():
    assert 1 == 1
