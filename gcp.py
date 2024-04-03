import subprocess
import sys
#import wget
import os.path
import requests

def duckdns_update(domains, token, ip, verbose=False):
    """Update duckdns.org Dynamic DNS record.
    Args:
        domains (str): The DuckDNS domains to update as comma separated list.
        token (str): An UUID4 provided by DuckDNS for your user.
        verbose (bool): Returns info about whether or not IP has been changed as
            well as if the request was accepted.
    Returns:
        "OK" or "KO" depending on success or failure. Verbose adds IP and change
        status as well.
    """
    params = {
        "domains": domains,
        "token": token,
        "ip": ip,
        "verbose": verbose
    }
    r = requests.get("https://www.duckdns.org/update", params)
    return r.text.strip().replace('\n', ' ')
token = "6b8ab0b3-d5c0-4928-b1b1-b9d19dbe3f98"
domain = "g3v.duckdns.org"

def download_key():
    #url_pub = "https://raw.githubusercontent.com/x3m030/g3v/main/google_compute_engine.pub"
    #url_prv = "https://raw.githubusercontent.com/x3m030/g3v/main/google_compute_engine"
    pub = '/.ssh/google_compute_engine.pub'
    prv = '/.ssh/google_compute_engine'
    loc = '/.ssh'

    #if os.path.exists(pub):
    #    os.remove(pub)bd268
    #if os.path.exists(prv):
    #    os.remove(prv)
    try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine.pub' ])  
         subprocess.run(['sudo', 'rm', '-rf', '/.ssh/google_compute_engine' ])     
    except:
         print(f"Failed to add user.")                    
         sys.exit(1)

    try:
        down = subprocess.run(['sudo', 'wget', 'https://raw.githubusercontent.com/x3m030/g3v/main/google_compute_engine.pub']) 
        down2 = subprocess.run(['sudo', 'wget', 'https://raw.githubusercontent.com/x3m030/g3v/main/google_compute_engine' ]) 
    except:
        pass
    subprocess.run(['sudo', 'mv', 'google_compute_engine.pub', '.ssh/' ])
    subprocess.run(['sudo', 'mv', 'google_compute_engine', '.ssh/' ])
# add user function
def add_user():

     # Ask for the input
     username = "g3c3p3"

     # Asking for users password
     password = "12345"

     try:
         # executing useradd command using subprocess module
         subprocess.run(['sudo', 'useradd', '-p', password, username ])     
     except:
         print(f"Failed to add user.")                    
         sys.exit(1)



def run_first():

     try:
         # executing useradd command using subprocess module
         r = subprocess.run(['gcloud', 'alpha', 'cloud-shell', 'ssh', '--dry-run' ],stdout=subprocess.PIPE)   
         a = r.stdout
         return a
         #print('gcp Done')
     except:
         print(f"Failed to create session.")                    
         sys.exit(1)


def run_wget():

     try:
         # executing useradd command using subprocess module
         subprocess.run(['pip3', 'install', 'wget'])
         print('Installing Wget Moldule Done')

     except:
         print(f"Wget Already Installed.")                    
         sys.exit(1)

try:
    add_user()
except:
    pass


run_wget()


run_first()


download_key()

res = run_first()
re = res.decode()
words, ss = re.split('=no ')


try:
    ips, ssss = ss.split(' -- DEVSHELL_PROJECT_ID')
    user,ip = ips.split('@')

    print ("""
           -----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEA3cLpsy8cicC9jKwGKHdbiiW8PG7oUpvaq94i8a/1FpMZ86DAOMWU
9otfHY+4TT7tcRslnjXh9NUidzdnyzmI2NpB68d7TIg8pkJLcWFnZqbM9RnzCOK0pP7Dk2
CJBOZhphr7u+SXMRMRyvMTdg6R0OJL24eyReiSazZ4BEDCEikAAAIA/mpsSP5qbEgAAAAH
c3NoLXJzYQAAAIEA3cLpsy8cicC9jKwGKHdbiiW8PG7oUpvaq94i8a/1FpMZ86DAOMWU9o
tfHY+4TT7tcRslnjXh9NUidzdnyzmI2NpB68d7TIg8pkJLcWFnZqbM9RnzCOK0pP7Dk2CJ
BOZhphr7u+SXMRMRyvMTdg6R0OJL24eyReiSazZ4BEDCEikAAAADAQABAAAAgAEeueVwyH
kdoxdxyvorWCgDdsbrXHsGVH1nus9zrw41If1sA2yF+vGf1JQmpKynM7XNiEwbQ4/j/6+Q
dRK+sKU9U//1HNaNiD6r1JVTsMabCWBDdFj71cLQh1dQOdUcErZxxWxFAflQpEWtHGFLBz
8o4QfEC18mYwudkBdyELEdAAAAQFlyoLkNH7xsWlzIkYp8gp0tCSelncBs1TxBVeLUmyyq
aTdhkRTWYHc0GVLwZBzgBUjE/YnNRdSAWvGC/qdNdxwAAABBAPreXnXp/9xtl0e4tZurKB
bVacZ3UWvza7awASbWhdWP+eL/NioRBvh81ibiRfrJaMMAWSe6Jv6oda1Ghnrz5IcAAABB
AOJMIPQkgcAS9ivf9AUTaT7F0EqAyqhzYUZoxNUKZ++zG/1PPwPPY6I/ooT+mn4YskXRla
cEWFVEclvJ2OoMr88AAAAGbm9uYW1lAQIDBAU=
-----END OPENSSH PRIVATE KEY-----
""")

    print("Here is Current INFO")

    print(ip + ":6000")

    print("username = g3c3p3")
    duckdns_update(domain, token, ip)

except:
      ips, ssss = ss.split(' --')
      user,ip = ips.split('@')

      print ("""
            -----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEA3cLpsy8cicC9jKwGKHdbiiW8PG7oUpvaq94i8a/1FpMZ86DAOMWU
9otfHY+4TT7tcRslnjXh9NUidzdnyzmI2NpB68d7TIg8pkJLcWFnZqbM9RnzCOK0pP7Dk2
CJBOZhphr7u+SXMRMRyvMTdg6R0OJL24eyReiSazZ4BEDCEikAAAIA/mpsSP5qbEgAAAAH
c3NoLXJzYQAAAIEA3cLpsy8cicC9jKwGKHdbiiW8PG7oUpvaq94i8a/1FpMZ86DAOMWU9o
tfHY+4TT7tcRslnjXh9NUidzdnyzmI2NpB68d7TIg8pkJLcWFnZqbM9RnzCOK0pP7Dk2CJ
BOZhphr7u+SXMRMRyvMTdg6R0OJL24eyReiSazZ4BEDCEikAAAADAQABAAAAgAEeueVwyH
kdoxdxyvorWCgDdsbrXHsGVH1nus9zrw41If1sA2yF+vGf1JQmpKynM7XNiEwbQ4/j/6+Q
dRK+sKU9U//1HNaNiD6r1JVTsMabCWBDdFj71cLQh1dQOdUcErZxxWxFAflQpEWtHGFLBz
8o4QfEC18mYwudkBdyELEdAAAAQFlyoLkNH7xsWlzIkYp8gp0tCSelncBs1TxBVeLUmyyq
aTdhkRTWYHc0GVLwZBzgBUjE/YnNRdSAWvGC/qdNdxwAAABBAPreXnXp/9xtl0e4tZurKB
bVacZ3UWvza7awASbWhdWP+eL/NioRBvh81ibiRfrJaMMAWSe6Jv6oda1Ghnrz5IcAAABB
AOJMIPQkgcAS9ivf9AUTaT7F0EqAyqhzYUZoxNUKZ++zG/1PPwPPY6I/ooT+mn4YskXRla
cEWFVEclvJ2OoMr88AAAAGbm9uYW1lAQIDBAU=
-----END OPENSSH PRIVATE KEY-----
""")

      print("Here is Current INFO")

      print(ip + ":6000")

      print("username = g3c3p3")
      duckdns_update(domain, token, ip)



print("""Auto Update Ip to duckdns was done...
      Server = g3v.duckdns.org
      Port = 6000
      UserName = g3c3p3
      Use Private Key to access server
      
      """)

print ("FREE GCP CloudShell")
