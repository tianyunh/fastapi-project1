import asyncio
from main import daysUntilNextHoliday


def test_daysUntilNextHoliday():
    assert asyncio.run(daysUntilNextHoliday("2021-09-03")) == {
        "Days until next U.S. Federal Holiday": 3
    }
    assert asyncio.run(daysUntilNextHoliday("2022-09-03")) == {
        "Days until next U.S. Federal Holiday": 2
    }
