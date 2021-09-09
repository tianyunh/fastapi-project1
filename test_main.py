import asyncio
from main import daysUntilNextHoliday

def test_daysUntilNextHoliday():
    assert asyncio.run(daysUntilNextHoliday("2021-09-03")) == {"Days until next holiday": 3}