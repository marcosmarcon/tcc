import numpy as np
import cv2
import time
import json
from openalpr import Alpr


alpr = Alpr("us", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
    
alpr.set_top_n(1)
alpr.set_default_region("md")

#results = alpr.recognize_file("/home/marcos/Desktop/apresentacao TCC/1.png")
#results = alpr.recognize_file("/home/marcos/Desktop/apresentacao TCC/2.png")
#results = alpr.recognize_file("/home/marcos/Desktop/apresentacao TCC/3.jpg")
results = alpr.recognize_file("/home/marcos/Desktop/apresentacao TCC/5.jpg")

i = 0

for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
	licPlate = results       
	
	with open('file-name.json') as data_file:    
    	    old_data = json.load(data_file)


	data = [{"placa": candidate['plate'],"dia": time.strftime("%d/%m/%Y"),"hora": time.strftime("%H:%M:%S")}]
	data = old_data + data
	path = '/home/marcos/Desktop/apresentacao TCC'
	filePathNameWExt =  path + '/' + 'file-name' + '.json'
    	with open(filePathNameWExt, 'w') as fp:
           json.dump(data, fp)




alpr.unload()
