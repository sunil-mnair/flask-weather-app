from datetime import datetime,timedelta
from pytz import timezone

unix_date = datetime.strptime('01-01-1970','%d-%m-%Y') + timedelta(hours=4)


def epoch_convertor(epoch):
    extracted_time_date = unix_date + timedelta(seconds=epoch)
    return extracted_time_date