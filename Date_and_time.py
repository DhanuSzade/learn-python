tz_NY=pytz.timezone('America/New_York')
datetime_NY=datetime.now(tz_NY)
print("NY:",datetime_NY.strftime("%m,%d,%Y,%H,%M,%S"))
