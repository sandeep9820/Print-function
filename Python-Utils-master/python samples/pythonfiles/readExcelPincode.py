import config
from copy import deepcopy
import csv

path = "../attachments/PinCode.csv"

file = open(path, "r")
reader = csv.reader(file)
dataList = []
count = 0
rows = list(reader)
for line in rows:
    # t=line[0],line[1],line[2]
    if line == rows[0]:
        continue
    data = {}
    data["pinCode"] = deepcopy(line[0])
    data["city"] = deepcopy(line[1])
    data["state"] = deepcopy(line[2])
    dataList.append(data)

print ("*"*80)
print dataList

