import xmltodict, json
import time
import schedule
import os
def runtestapi():
	os.system('make test-report')
	os.system('make test-api')
	with open('test-results.xml', 'r') as myfile:
    		obj = xmltodict.parse(myfile.read())
	f=open('results.json', 'w')
	f.write(json.dumps(obj))
	f.close()
	os.system('curl http://194.182.163.0:8088/services/collector/raw -H "Authorization: Splunk 1963304e-0360-4a39-8bb8-1f89e3d5150c" -d @results.json')
	time.sleep(1)
	os.system('curl http://194.182.163.0:8088/services/collector/raw -H "Authorization: Splunk 1963304e-0360-4a39-8bb8-1f89e3d5150c" -d @tests/outputfile.json')
schedule.every(1).minutes.do(runtestapi)
while True:
	schedule.run_pending()
	time.sleep(1)

