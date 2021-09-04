from fastapi import FastAPI
import uvicorn

import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar


app = FastAPI()

dates = pd.DataFrame({'date':pd.date_range('2021-01-01', '2022-01-01')})
cal = calendar()
holidays = cal.holidays(start=dates["date"].min(), end=dates["date"].max())

@app.get("/")
async def root():
    return {"message": "Please enter a date in 2021 with the format 'yyyy-mm-dd' to see how far the next holiday is!"}

@app.get("/HolidayTime/{date}")
async def daysUntilNextHoliday(date: str):
    """Calculate Days Until Next U.S. Federal Holiday"""
    date = pd.to_datetime(date, format='%Y-%m-%d')
    difference=[]
    if (date > pd.to_datetime('2021-12-31', format='%Y-%m-%d')) or (date < pd.to_datetime('2021-01-01', format='%Y-%m-%d')):
        return {"Days until next holiday": "Oops! Date is not in 2021."}
    else:
        for day in holidays:
            difference.append(int(str((day-date).days)))
        return {"Days until next holiday": min([x for x in difference if x>=0])}
        

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    