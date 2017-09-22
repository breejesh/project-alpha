import json
import os
data = None
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	if f.find(".json") != -1:	
		with open(f) as data_file:    
		    data = json.load(data_file)
		print f, len(data)

