README

WANem controller is a two part system

wanemconf.py - parses config file and outputs csv file for wanemrun

wanemrun.py - reads csv file and sends commands to WANem webserver

Requirements:

mechanize: install using "easy_install mechanize"

Usage:

python wanemconf.py inputconf outputcsv

python wanemrun.py serverhostname|serverip inputcsv

Configuration: see sample .conf files
	time interface [subconfig] parameter=value[;parameter=value]