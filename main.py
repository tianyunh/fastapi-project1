from fastapi import FastAPI
import uvicorn

import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar


app = FastAPI()



@app.get("/")
async def root():
    return {
        "message": "Please enter a date with the format 'yyyy-mm-dd' to see how far the next holiday is!"
    }


@app.get("/HolidayTime/{date}")

async def daysUntilNextHoliday(date: str):
    """Calculate Days Until Next U.S. Federal Holiday"""
    date = pd.to_datetime(date, format="%Y-%m-%d")
    year = date.year
    start = str(year)+"-01-01"
    end = str(year+1)+"-01-01"
    dates = pd.DataFrame({"date": pd.date_range(start, end)})
    cal = calendar()
    holidays = cal.holidays(start=dates["date"].min(), end=dates["date"].max())
    
    difference = []
    
    for day in holidays:
        difference.append(int(str((day - date).days)))
    
    return {"Days until next U.S. Federal Holiday": min([x for x in difference if x >= 0])}



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
