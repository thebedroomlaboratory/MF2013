import dao
import random
import time

dao.connect()

while(True):

	data=[random.randint(0, 10), random.randint(0, 1)]
	dao.insertRow('people', data)

	data=[random.randint(2500, 20000), random.randint(0, 1)]
	dao.insertRow('oven', data)

	data=[random.randint(0, 1), random.randint(0, 700), random.randint(0, 3000), random.randint(0, 1)]
	dao.insertRow('temp', data)

	time.sleep(2);

dao.disConnect()
