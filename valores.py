#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importando los  modulos a usar
import urllib2
import simplejson
import json 

#esta es la url donde esta el archivo json 
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
 
# Se formatea el resultado de lo requerido 
print 'bitcoin   | dolartoday'
print '%s | %s' % (rk[0], ' '+ rk[1])
print '-' * 30
print str(rv[0]), '       |        ' + str(rv[1])
