import dao


dao.connect()

data=[6, 1]
dao.insertRow('people', data)

data=[6, 1]
dao.insertRow('oven', data)

data=[6, 1, 3, 5]
dao.insertRow('temp', data)


dao.disConnect()
