#/usr/bin/python3
import requests
import nmap
import json
import time
import sys

ips = sys.argv[1]

fips = open(ips, "r"); lips = fips.read().splitlines(); fips.close();

for ip in lips:
	getjson = requests.get("http://ip-api.com/json/"+str(ip))
	response = json.loads(getjson.text)
	response['host'] = ip
	queryIP = response['query']
	try:
		portScan = nmap.PortScanner()
		scanResult = portScan.scan(queryIP, '80')
		response['stateIP'] = portScan[queryIP].state()
	except Exception as e:
		response['stateIP'] = 'N/A'

	finw = open("resultIPNmap.json", "a+")
	finw.write(json.dumps(response)+"\n")
	time.sleep(1.5)
	print(json.dumps(response))
