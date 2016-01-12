import re
import mechanize

br = mechanize.Browser()
br.open("http://10.154.32.150/WANem/start_advance.php")
br.select_form(nr=0);

br["selInt"] = ["eth1"]

br.submit();
br.select_form(nr=0);
br["txtDelay1"] = "101"


#br.form.find_control("btnApply").readonly = False

#br.form.find_control("btnAdd").disabled = True
#br.form.find_control("btnReset").disabled = True
#br.form.find_control("btnRefresh").disabled = True
#br.form.find_control("btnStopNetem").disabled = True

print br.form
import sys, logging

#logger = logging.getLogger("mechanize")
#logger.addHandler(logging.StreamHandler(sys.stdout))
#logger.setLevel(logging.DEBUG)


#br.set_debug_http(True)
#br.set_debug_responses(True)
#br.set_debug_redirects(True)
for control in br.form.controls:
	print control.value

br.submit("btnApply")