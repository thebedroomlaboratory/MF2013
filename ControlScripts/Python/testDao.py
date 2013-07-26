import dao
import random

dao.connect()

data=[random.randint(1, 10), random.randint(1, 10)]
dao.insertRow('people', data)

data=[random.randint(1, 10), random.randint(1, 10)]
dao.insertRow('oven', data)

data=[random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
dao.insertRow('temp', data)


dao.disConnect()
