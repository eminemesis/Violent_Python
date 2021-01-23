from socket import *
import optparse
from threading import Thread, Semaphore

lock=Semaphore(1) #Semaphore restricts the threads from printing to the screen at the same time
def connScan(host, port): #create a socket, ping the address and grab the banner
    try:
        skt=socket(AF_INET, SOCK_STREAM) #AF_INET = IPV4, SOCK_STREAM=TCP
        skt.settimeout(2)
        skt.connect((host, int(port)))
        skt.send('RandomGibberish\n'.encode('utf-8')) #Linux implicitly encodes the message, Windows needs explicit encoding
        msg=skt.recv(150) #adjust the value per your needs
        lock.acquire() #the section above is executed in parallel, the section below is locked until the thread releases the lock
        print('[+] {}/{} is open \nMsg: {} \n'.format(host, port, msg))
        skt.close()
    except Exception as e:
        print(str(e)+'\n')
        lock.acquire() #acquiring lock for exception case output
        print('[-] {}/{} is closed\n'.format(host, port))
        skt.close()
    finally:
        lock.release() #releasing lock on output screen as the thread is executed

def portScan(host, ports): #iterate connScan through the list of ports
    try:
        host_ip=gethostbyname(host)
        print('\nScanning '+host+'\n')
        for port in ports:
            trd=Thread(target=connScan, args=(host_ip, port)) #threading the connections for efficiency
            trd.start()
    except Exception as e:
        print('Please check the host name. Refer following for more details.\n')
        print(e)

def main():
    parser=optparse.OptionParser()
    def port_splitter(option, opt, value, parser):
        setattr(parser.values, option.dest, value.split(','))
    parser.add_option('-H', dest='host', type='string', help='target host')
    parser.add_option('-P', type='string', help='target ports [comma seperated]', action='callback', callback=port_splitter, dest='ports')
    options, args=parser.parse_args()
    host=options.host
    ports=options.ports
    portScan(host, ports)

if __name__=='__main__':
    main()
