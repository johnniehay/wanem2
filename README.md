# WANem-controller
A time driven WANem controller

[Wiki](https://github.com/johnniehay/WANem-controller/wiki)

WANem controller is a two part system

*wanemconf.py* - parses config file and outputs csv file for wanemrun

*wanemrun.py* - reads csv file and sends commands to WANem webserver

Requirements:

  *python-2.7:* or high except python3
  *mechanize:* install using "easy_install mechanize"

Usage:

>python wanemconf.py inputconf outputcsv

>python wanemrun.py serverhostname|serverip inputcsv

Configuration: [Config format](https://github.com/johnniehay/WANem-controller/wiki/Config-format)
>	time interface [subconfig] parameter=value[;parameter=value]
see sample .conf files
