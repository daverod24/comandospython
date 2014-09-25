#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import simplejson
import json 
 
url = "http://api.bitven.com/prices"
 
resp = urllib2.Request(url)
opener = urllib2.build_opener()
data = opener.open(resp)
result = simplejson.load(data)
rk=result.keys()
rv=result.values()
 
#print result
print 'bitcoin   | dolartoday'
print '%s | %s' % (rk[0], ' '+ rk[1])
print '-' * 30
print str(rv[0]), '       |        ' + str(rv[1])
