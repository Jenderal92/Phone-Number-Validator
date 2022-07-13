#Phone Number Validator
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#You can recode This Tools 
#But I beg you not to delete the author's name.

import requests,re,time,random ,os, sys, base64,json
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore,init
init(autoreset=True)


def NUM_V(url):
	try:
		ua = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Origin': 'https://randommer.io',
		'Cookie': 'ezoadgid_232529=-1; ezoref_232529=; ezosuibasgeneris-1=1b419369-2d34-4556-7136-18952258d734; ezoab_232529=mod31; ezepvv=115; ezovid_232529=1256499834; lp_232529=https://randommer.io/Phone/Validator; ezovuuid_232529=1c271cc1-64ec-4a3c-7b84-8c897b113eba; ezouspvv=0; ezouspva=0; ezds=ffid%3D2%2Cw%3D393%2Ch%3D873; ezohw=w%3D393%2Ch%3D789; __qca=P0-1261743123-1655977847176; ezux_lpl_232529=1655977847995|a5fdd911-9a1e-4b73-56e3-ed544c10fda1|false; __gads=ID=365d995528503800:T=1655977848:S=ALNI_MZo1ctDrRg5-MiIduy3kAzcjxlPzA; __gpi=UID=000006e4a9a80061:T=1655977848:RT=1655977848:S=ALNI_MZpy6O2_91J47jR2zNxcEy9GfPg7Q; _pbjs_userid_consent_data=3524755945110770; ezux_ifep_232529=true; ezux_et_232529=16; active_template::232529=pub_site_mobile.1655979401; ezopvc_232529=3; ezovuuidtime_232529=1655979403; ezux_tos_232529=357'
		}
		data = {'twoLettersCode': code_country,
		'Telephone': url,
		'X-Requested-With': 'XMLHttpRequest'
		}
		SHINGET = requests.post("https://randommer.io/Phone/Validator", data=data ,headers=ua).content
		if 'true' in SHINGET:
			print(Fore.GREEN + '[VALID --> ]' + Fore.WHITE + url +'|'+ str(SHINGET))
			open('Valid.txt','a').write(url+'\n')
		if 'false' in SHINGET:
			print(Fore.RED + '[INVALID --> ]' + Fore.WHITE + url +'|'+ str(SHINGET))
			open('Invalid.txt','a').write(url+'\n')
	except:
		pass

print "{}Phone Number Validator  | Shin Code".format(Fore.YELLOW)
print "{}ICQ : https://icq.im/Shin403\n".format(Fore.YELLOW)
url = open(raw_input(Fore.WHITE+'List:~# '),'r').read().splitlines()
code_country = raw_input("Country Exp: US : ")
pool = ThreadPool(20)
pool.map(NUM_V, url)
pool.close()
pool.join()