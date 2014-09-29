#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  urlquery.py
#  
#  Copyright 2014 david <david@david-linux1>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import urllib2, cookielib
import simplejson
import json
import requests
from pyquery import PyQuery


def main():
	USER_AGENT = 'Mozilla/5.0'
	coinbase_URL = 'http://www.coinbase.com'
	cb = coinbase_URL
	headers = {'User-Agent': USER_AGENT}
	##urlib html
	resp = urllib2.Request(cb)
	opener = urllib2.build_opener()
	#aqui obtenemos la data
	data = opener.open(resp)

	cba = PyQuery(requests.get(cb, headers=headers).content).find('.top-balance').text().replace('Buy Price: ', '')

	print cba
	
	return cba

if __name__ == '__main__':
	main()

