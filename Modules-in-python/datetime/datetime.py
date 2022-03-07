import datetime   

# 1) datetime.datetime.now() = give time and date info 

print(datetime.datetime.now())

# 2) datetime.datetime.today() = give time and date info

print(datetime.datetime.today())

# Difference between now() and today() is now() can give time & date info of differnt timezone also by take required argument but today() only give the local timezone info

# 3) datetime.datetime.now().year | .month | .day | .minute | .second | .microsecond

print(datetime.datetime.now().day)
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)
print(datetime.datetime.now().hour)

# 4) datetime.datetime.now().strftime() = format output accordingly

print(datetime.datetime.now().strftime("%d-%m"))

# 5) datetime.datetime.fromtimestamp() = convert seconds into date
 
print(datetime.datetime.fromtimestamp(2344523343))

# 6) datetime.datetime.timestamp() = convert date into seconds

x = datetime.datetime.now()

print(datetime.datetime.timestamp(x))