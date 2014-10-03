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
import urllib2
import simplejson
import json
import android,sys
droid=android.Android()
#from pprint import pprint
#import requests
#from pyquery import PyQuery
rv=''
rk=''
mb=''
ecu1=''


def btcval():
	#esta son urls donde estan los archivos json 
	url = "http://api.bitven.com/prices"
	
	#Aqui usamos urllib2 para abrir la pagina 
	resp = urllib2.Request(url)
	opener = urllib2.build_opener()
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
	
	

	
		
		 
	# Se formatea el resultado de lo requerido 
	print '*******************************************'
	print 'Tasas del mercado actual de divisas        '
	print '*******************************************'
	print 'Bitcoin    |   Dolartoday   |  Bolivar     '
	print '*******************************************'
	print str(rv[0]),' ฿ ' ' | ' + str(rv[1]),' $. ' ' | '+str(mb), ' Bs. '
	print '*******************************************'
	
	rvb = rv[0]
	rvus = rv[1]
	
	#Se muestra la informacion del contacto seleccionado
	droid.dialogCreateAlert('  Btc,  usd,  vef  ',' ฿  %s,    %s, $     %s Bs. ' %(rvb, rvus, mb) )
	#Se crea el botón aceptar
	droid.dialogSetPositiveButtonText('Aceptar')
	#Se muestra la ventana
	droid.dialogShow()

	return 0
		
		
btcval()

