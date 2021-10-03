import requests
import time

epoch_time = int(time.time())

url = "https://weerindelft.nl/clientraw.txt?" + str(epoch_time)

page = requests.get(url)
list_param = page.text.split()
temperature = round(float(list_param[4]))

print(str(temperature) + " degrees Celsius")