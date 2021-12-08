from selenium import webdriver
import time
import datetime
now = datetime.datetime.now() - datetime.timedelta(hours=1) - datetime.timedelta(minutes=17)

# Determine if anymore active listings
if now.hour <= 7:
    print("no notting to see")
    exit()
elif now.hour == 21 & now.minute >= 43:
    print("just missed the bus matey")
    exit()
elif now.hour >= 22:
    print("it's late m8")
    exit()
else:
    print("searching...")

# Make correct format time
timestamp = "{:4d}-{:02d}-{:02d}T{:02d}{:02d}".format(now.year, now.month, now.day, now.hour, now.minute)


# Just for test
# testihaku = "exportTrades('NordicEquity-posttrade-2021-12-01T2125')"


# JavaScript execution for commandline
JSx = ("exportTrades('NordicEquity-posttrade-"+timestamp+"')")

# Start Chrome Driver
chromedriver = "C:/Users/Pon/Documents/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(chromedriver)

# Open URL
URL = 'http://www.nasdaqomxnordic.com/shares/equities'
driver.get(URL)

# Execute JS - do some sleeping magic
time.sleep(4)
driver.execute_script(JSx)
time.sleep(4)
# Remember to close chrome driver browser
driver.quit()
