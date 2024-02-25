import time
import datetime
import json
import sys
import requests


def belltime(path):
	with open(path) as fh:
                j_obj = json.load(fh)
	h = datetime.datetime.now().strftime("%H")
	m = int(int(datetime.datetime.now().strftime("%M"))/15.0)
	l = datetime.datetime.now().strftime("%Y%m%d:%H%M%S")
	print("One of ", j_obj[h], " with ", m)
	print("Specifically ", j_obj[h][m])
	r = requests.get("http://spare2:8000/slow/"+str(j_obj[h][m]))
#	with open("/home/bob/bell.log","a") as lf:
#		lf.write(l+" "+str(j_obj[h][m])+"\n")
#	print(json.dumps(j_obj))
#	for k in j_obj:
#		v = j_obj[k]
#		print("At ",k," do ", v)
#		for m in range(0,4):
#			n = v[m]
#			print(">>> At ",k,":",m," do ", n)

if __name__ == '__main__':
        belltime(sys.argv[1])

