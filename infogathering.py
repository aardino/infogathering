#!/usr/bin/python
#--*--encoding:utf-8--*--

#author:Antoine ARDINO

import urllib2

def get_dns(lien):
	
	print "Récuperation des DNS de " + lien

	try:
		url = 'https://api.hackertarget.com/dnslookup/?q='+lien
		cont = urllib2.Request(url)
		conte = urllib2.urlopen(cont)
		content = conte.read()
		print content
	except : 
		print "Erreur. Veuillez réessayer plus tard"


def whois(lien):
	
	print "Démarrage de WHOIS sur " + lien

        try:
                url = 'https://api.hackertarget.com/whois/?q='+lien
                cont = urllib2.Request(url)
                conte = urllib2.urlopen(cont)
                content = conte.read()
                print content
        except : 
                print "Erreur. Veuillez réessayer plus tard"


def geoip(lien):

        print "Géo ip de " + lien

        try:
                url = 'https://api.hackertarget.com/geoip/?q='+lien
                cont = urllib2.Request(url)
                conte = urllib2.urlopen(cont)
                content = conte.read()
                print content
        except : 
                print "Erreur. Veuillez réessayer plus tard"


def robots(lien):

        print "Robots.txt de "+lien

        try:
                url = lien + '/robots.txt'
                cont = urllib2.Request(url)
                conte = urllib2.urlopen(cont)
                content = conte.read()
                print content
        except : 
                print "Pas de fichiers Robots sur ce site."

def subnet(lien):

        print "Subnet de " + lien

        try:
                url = 'https://api.hackertarget.com/subnetcalc/?q='+lien
                cont = urllib2.Request(url)
                conte = urllib2.urlopen(cont)
                content = conte.read()
                print content
        except : 
                print "Erreur. Veuillez réessayer plus tard"


def scanport(lien):

        print "Scanner de ports de " + lien

        try:
                url = 'https://api.hackertarget.com/nmap/?q='+lien
                cont = urllib2.Request(url)
                conte = urllib2.urlopen(cont)
                content = conte.read()
                print content
        except : 
                print "Erreur. Veuillez réessayer plus tard"

url = raw_input("Lien du site : ")


print "Que faire ? "
print "[1] DNS"
print "[2] WHOIS"
print "[3] Geo IP"
print "[4] Robots.txt"
print "[5] Subnet Lookup"
print "[6] Scanner de ports"
choix = input(">")

if choix == 1:
	get_dns(url)
elif choix == 2:
	whois(url)
elif choix == 3:
	geoip(url)
elif choix == 4:
	robots(url)
elif choix == 5:
	subnet(url)
elif choix == 6:
	scanport(url)
else:
	print "Choix incorrect"
