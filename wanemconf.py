
#	^(\d*)\s*(\w*[ ])?(\d*[ ])?(?:(\w*)=(\w*);?)+\s*[/]*.*$
#	^(\d*)\s*(\w*[ ])?(\d*[ ])?([^ ]*)\s*[/]*.*$
#	^(\d*)\s*(\w*)[ ]?(\d*)\s*([^ ]*).*$

import re
import csv
import sys

dkey = {	"delay" 	:	"txtDelay",
	 	"loss"		:	"txtLoss",
	 	"jitter"	:	"txtDelayJitter",
		"bandwidth"	:	"txtBandwidth"
	}
if len(sys.argv) != 3:
	print "Usage: wanemconf inputconf outputcsv"
	sys.exit()
	
with open(sys.argv[1],'rb') as inf:
	conf = inf.readlines()
	print "Input confugration:"
	c = []
	for line in conf:
		print "\t",line,
		m = re.match(r"^([\d.]*)\s*(\w*)[ ]?(\d*)\s*(\S*).*$", line)
		cl = list(m.groups())
		if cl[1] == "command":
			#print "command:", line
			line = line.rstrip("\n")
			cl[2] = line[line.find(" command ")+len(" command "):]
			if cl[2].startswith('"') and cl[2].endswith('"'):
   				cl[2] = cl[2][1:-1]
				#print cl[2]
			cl[3] = [ ]
		
		if cl[3]:
			cl[3] = cl[3].split(';')
			# Split and validate the line 
			for part in range(len(cl[3])):
				cl[3][part] = cl[3][part].split("=")
			#print cl
		c.append(cl)
	c.sort(key=lambda x:float(x[0]))
	#print c
	
headlist = ["time","interface","subconfig"]
for l in range(len(c)):
	for p in range(len(c[l][3])):				# Substitute keywords for html form control names using d
		if c[l][3][p][0] in dkey:
			c[l][3][p][0] = dkey[c[l][3][p][0]]
			if c[l][3][p][0] not in headlist:
				headlist.append(c[l][3][p][0])
		else:
			if c[l][3]:
				print "Parameter %s not found" % repr(c[l][3][p][0])
#		print c[l][3][p][0]
#print c

#print headlist
parmlist = []


for l in c:										#Build csv dictionary
	if l[3]:
		d = dict(l[3])
	else:
		d = dict()
	d["time"] = l[0]
	d["interface"] = l[1]
	d["subconfig"] = l[2]
	if not l[2]:
		d["subconfig"] = "1"
	parmlist.append(d)
	#print d
	#for p in headlist:
	#	if next((x[1] for x in l[3] if p in x[0]), None):
	#		print "Got:", p , "in", l
	
#print parmlist;
	
with open(sys.argv[2],"wb") as outf:			# Write to csv file
    writer = csv.DictWriter(outf, fieldnames=headlist)
    writer.writeheader()
    for di in parmlist:
        writer.writerow(di)
		
print "Output configuration:"
with open(sys.argv[2],"rb") as outf:			# Read out csv file
	outc = outf.readlines()
	for l in outc:
		print "\t",l,
print "Written to", sys.argv[2]