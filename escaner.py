#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test de velocidad Raspberry + Twitter
by @yo @thechapu

"""
import csv
import datetime
import os
import time
import twitter


def test():
        print 'Corriendo speedtest...'
        a = os.popen("speedtest --simple").read()
        print 'Speedtest completado:'
        # Separamos en 3 lineas el resultado (ping,down,up)
        lines = a.split('\n')
        print a # print resultado
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        # Si speedtest No se pudo conectar o la velocidad es 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        # Extraer los valores de ping down y up.
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print "Fecha : ",date, "Ping : ",p,"Download : ", d,"Upload : ",u
        # Guardar los datos en la raspberry para luego graficar
        # Agregar directorio donde guardar archivo, por defecto home
        out_file = open('speedtest.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((date, p, d, u))
        out_file.close()

        # Twitter Credenciales
        api = twitter.Api(consumer_key='TU CONSUMER KEY',
                  consumer_secret='TU CONSUMER SECRET',
                  access_token_key='TU TOKEN KEY',
                  access_token_secret='TU TOKEN SECRET')


        # Tweet si la velocidad inicial es menos lo que yo puse
        # Debemos agregar la velocidad que nos "Promete" el proveedor de Internet, en mi Caso 50 mg
        if eval(d) < 50: # Reemplazar velocidad aqui
                print "Tuiteando internet lento."
                try:
                		# Debomos buscar el Twitter de nuestro proveedor (en mi caso Movistar) y cambiar donde dice "50/5" por el servicio que tengan contratado
                        # ENVIAMOS TWIT
                        status = api.PostUpdate("Porque mi #velocidad #internet es :  " + str(int(eval(d))) + " down\\" + str(int(eval(u))) + " up cuando pago por 50\\5 en #Movistar #speedtest")
                except Exception, e:
                        print str(e)
                        pass
        return

if __name__ == '__main__':
	try:
		test()
		print 'Completed!'
	except Exception, e:
		print e
