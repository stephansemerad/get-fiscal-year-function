import dateutil.relativedelta
from datetime import datetime

# example. get_start_end_fiscal_year('30.09.')
def get_start_end_fiscal_year(day_month=''):
    fy_end = datetime.strptime(str(day_month+str(datetime.now().strftime('%Y'))), "%d.%m.%Y")
    fy_start = fy_end - dateutil.relativedelta.relativedelta(months=11) + dateutil.relativedelta.relativedelta(day=1)
    return [fy_start.strftime('%d-%m-%Y'), fy_end.strftime('%d-%m-%Y')]


print  (get_start_end_fiscal_year('30.09.'))
