import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in data if "All User profiles" in i]
for i in profiles:
    
    try:
        results = subprocess.check_output(['netsh','wlan','show','profiles',i, 'key*clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key content" in b]
        print("{:<30}|{:<}".format(i,results[0]))
    except IndexError:
        print("{:<30}|{:<}".format(i,"")) 
    except subprocess.CalledProcessError:
        print("{:<30}|{:<}".format(i,"ENCODING ERROR"))

input("")  

