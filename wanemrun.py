import os
import re
import csv
import sys
import time
import mechanize
starttime = time.time()
early = 0.2
if len(sys.argv) != 3:
	print "Usage: wanemrun serverhostname|serverip inputcsv"
	sys.exit()

ifile  = open(sys.argv[2], "rb")
reader = csv.reader(ifile)
interface = ""
br = None
rownum = 0
for row in reader:
	# Save header row.
	if rownum == 0:
		header = row
	else:
		shcommand = ""
		colnum = 0
		for col in row:
			if colnum == 0:
				nexttime = float(col)
				print "nexttime: ", nexttime, starttime+nexttime
			elif colnum == 1:
				if col == "command":
					shcommand = col
					print "c:" , col
					colnum += 1
					continue
				elif interface != col:
					if br:
						br.close()
					br = mechanize.Browser()
					br.open("http://"+sys.argv[1]+"/WANem/start_advance.php")
					br.select_form(nr=0)
					interface = col
					br["selInt"] = [col]
					br.submit()
				br.select_form(nr=0)
				print "interface: ", interface
			elif colnum == 2:
				if shcommand:
					print "command:", col
					shcommand = col
					break
				subconf = col
				if subconf > 1 and (header[3] + subconf) not in br.form.__str__():
					print "Adding new subconf"
					br.submit("btnAdd")
					br.select_form(nr=0)															
				print "subconf: ", subconf
			else:
				if col:
					if isinstance(br[header[colnum] + subconf], basestring) :
						br[header[colnum] + subconf] = col
					else:
						br[header[colnum] + subconf] = [col]
					print "br[" + header[colnum] + subconf + "] =" + col 
			colnum += 1	
		
		if starttime+nexttime-early > time.time():
			print time.time()
			time.sleep(starttime+nexttime-early-time.time())
			print time.time()

		
		
		#br["txtDelay1"] = "101"


		#br.form.find_control("btnApply").readonly = False

		#br.form.find_control("btnAdd").disabled = True
		#br.form.find_control("btnReset").disabled = True
		#br.form.find_control("btnRefresh").disabled = True
		#br.form.find_control("btnStopNetem").disabled = True

		#print br.form
		import sys, logging

		#logger = logging.getLogger("mechanize")
		#logger.addHandler(logging.StreamHandler(sys.stdout))
		#logger.setLevel(logging.DEBUG)


		#br.set_debug_http(True)
		#br.set_debug_responses(True)
		#br.set_debug_redirects(True)
		#for control in br.form.controls:
			#print control.value
		print time.time()
		if shcommand:
			print "Shell running", shcommand
			os.system(shcommand)
		else:
			br.submit("btnApply")
			print "Submitting:" , time.time(), time.time()-starttime-nexttime
		#br.close()
	rownum += 1
		