import asyncio
from main import daysUntilNextHoliday


def test_daysUntilNextHoliday():
    assert asyncio.run(daysUntilNextHoliday("2021-09-03")) == {
        "Days until next holiday": 3
    }
    assert asyncio.run(daysUntilNextHoliday("2022-09-03")) == {
        "Days until next holiday": "Oops! Date is not in 2021."
    }
