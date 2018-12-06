
import dateutil.relativedelta; from datetime import datetime
today = datetime.now()
fiscal_year  = '30.09.'
current_year = datetime.now().strftime('%Y')
fy           = datetime.strptime(fiscal_year+current_year, "%d.%m.%Y")
if fy < today: current_year = str(int(current_year) + 1)
fy          = datetime.strptime(fiscal_year+current_year, "%d.%m.%Y")
fy_end      = fy
fy_start    = fy_end - dateutil.relativedelta.relativedelta(months=11) + dateutil.relativedelta.relativedelta(day=1)
fy_end      = fy_end.strftime('%Y-%m-%d')
fy_start    = fy_start.strftime('%Y-%m-%d')
