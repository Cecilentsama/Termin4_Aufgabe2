from datetime import date
from common.functions import age_from_date


def test_age_from_date():
    assert age_from_date(date.today()) == 0
    d1 = date.today()
    d1 = d1.replace(year=d1.year - 1)
    assert age_from_date(d1) == 1
    d2 = date.today()
    d2 = d2.replace(month=d2.month - 1)
    assert age_from_date(d2) == 0
