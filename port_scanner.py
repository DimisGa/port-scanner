import socket
import argparse 
from colorama import Fore

#### basic port scanner ####


### the conn function connects to a server
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def conn(ip,port):

	s.connect((ip,port))
	s.send("data\n\r".encode('utf-8'))
	banner=s.recv(1024)
	return banner	



### this function checks if the router is vulnerable
def check(ip,banner,file):
	

	f=open(file,"r")

	print(banner.decode('utf-8'))
	print("\n[*] Checking For Vulnerabilities...")
	for line in f.readlines():
		
		line=line.strip("\n")

		if(line in str(banner)):
			print(Fore.GREEN+"\n[*] Server "+str(ip)+" is Vulnerable!")
			break
		else:
			print(Fore.RED+"\n[-] Server Not Vulnerable...")


def main():

	### The main program starts by parsing our flags

	parser=argparse.ArgumentParser()
	parser.add_argument("-t",dest="Target",type=str,help="target ip to scan")
	parser.add_argument("-p",dest="Port",type=int,help="target port to scan")
	parser.add_argument("-f",dest="File",type=str,help="file to check vulnerabilities")
	args=parser.parse_args()

	ip=args.Target
	port=args.Port
	file=args.File


	## the the check function is called thus printing the banner
	## as well as checking it against the file
	
	check(ip,conn(ip,port),file)

main()