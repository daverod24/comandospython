#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  valores btc usd y VEB
#  
#  Copyright 2014 David Rodriguez <davidrodriguez at gmail dot com>
#  el  api es gracias a la gente de bitven.com @diariobitcoin y dolartoday 
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



#importando los  modulos a usar
import urllib2, cookielib
import simplejson
import json
from pprint import pprint
import requests
from pyquery import PyQuery
rv=''
rk=''
mb=''
ecu1=''


def btcval():
	#esta son urls donde estan los archivos json 
	url = "http://api.bitven.com/prices"
	urlbdt = "http://api.bitcoinvenezuela.com/DolarToday.php?json=yes"
	#Aqui usamos urllib2 para abrir la pagina 
	resp = urllib2.Request(url)
	opener = urllib2.build_opener()
	###############################
	jbtcven = urllib2.urlopen(urlbdt)
	jbv = json.load(jbtcven)
	val= jbv.values()
	key= jbv.keys()
	
	#################################
	#aqui obtenemos la data
	data = opener.open(resp)
	#en este punto  decodificamos la data y podemos separar lo que necesitemos 
	result = simplejson.load(data)
	# Se separa las llaves 
	rk=result.keys()
	# Se separan los valores
	rv=result.values()
	# se  multiplica los  valores para tener el valor del Bolivar 
	mb= rv[1]*rv[0]
	
	# precio de el bitcoin dado por coinbase
	USER_AGENT = 'Mozilla/5.0'
	coinbase_URL = 'http://www.coinbase.com'
	cb = coinbase_URL
	headers = {'User-Agent': USER_AGENT}
	##urlib html
	resp = urllib2.Request(cb)
	opener = urllib2.build_opener()
	#aqui obtenemos la data
	data = opener.open(resp)

	cba = PyQuery(requests.get(cb, headers=headers).content).find('.top-balance').text().replace('Buy Price: $', '')

	
		
		 
	# Se formatea el resultado de lo requerido 
	print '********************************************'
	print 'Tasas del mercado actual de divisas        '
	print '********************************************'
	print 'Bitcoin    |    Dolartoday     |  Bolivar ' 
	print '********************************************'
	print str(rv[0]),' ฿ ' '  |  ' + str(rv[1]),' $. ' ' |  '+str(mb), ' Bs. '
	print '********************************************'
	print '                                          '
	print '                                          '
	print '                                          '
	print '                                          '
	print '********************************************'
	print '    Ecuaciones de compra eficiente de btc   '
	print '********************************************'
	print '* formula usada:                            *'
	print '* coinbaseusd_ask*dolartoday*1,3            *'
	print "*  precio coinbase    ", cba, "$             *"
	coinbaseusd_ask = cba
	dl=rv[1]
	com=1.03
	ecu1= float(coinbaseusd_ask)*dl*com
	print "* serian " , ecu1,"bolivares por bitcoin *"
	print "*                                           *"
	print '*                                           *'	
	
		
	return 0
		
		
btcval()


