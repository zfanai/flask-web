#!usr/bin/python
#-*- coding: utf-8 -*-
import sys
from app import create_app

app=create_app()
app.debug = True

#外部可见
if __name__ == "__main__":
	#app.run(host='localhost', threaded=False, port=8081)
	app.run(host = '0.0.0.0', threaded=False, port=8081)
