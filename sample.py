from datetime import timedelta, datetime
import time

def equal(dt1, dt2):
    return dt1.replace(second=0, microsecond=0) == dt2.replase(second=0, microsecond=0)



time.strftime("%w") #[0,6] voskres 0

time.strftime("%u") #[1, 7] poned 1

datetime.date.weekday() #[0,6] poned 0

datetime.date.isoweekday() #[1, 7] poned 1

a = datetime

calendar.weekday() #[0, 6] poned 0

