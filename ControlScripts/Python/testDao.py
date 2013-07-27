import dao
import random
import time

dao.connect()

data=[random.randint(1, 10), random.randint(1, 10)]
dao.insertRow('people', data)

data=[random.randint(1, 10), random.randint(1, 10)]
dao.insertRow('oven', data)

data=[random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
dao.insertRow('temp', data)

time.sleep(2);

dao.disConnect()
