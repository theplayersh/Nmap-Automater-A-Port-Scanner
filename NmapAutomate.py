import os
import sys
import time

#NMAP AUTOMATER

print "Installing Requirements..."
os.system("sudo apt-get install figlet")
os.system("pkg install figlet")
#Figlet installed
os.system("sudo apt-get install nmap")
os.system("pkg install nmap")
#Nmap installed

os.system("clear")
os.system("figlet -f slant NMAP AUTOMATE")
print "----------------------------------------------------"
print ""
print "[1] Scan A Website "
print "[2] Scan a ip Address"
print "[3] Advanced Options"
print "[4] About The Tool"
print ""
print "[99] Exit"
print ""
op=raw_input("Root@Nmap:~$")

def logo():
	os.system("figlet -f slant NMAP AUTOMATE")

def cls():
	os.system("clear")

if op == '1' or op == '01':
	cls()
	logo()
	print ""
	website=raw_input("Which Website You want To Scan :")
	os.system("nmap -v -A %s" % (website))

if op == '2' or op == '02':
	cls()
	logo()
	print""
	wep=raw_input("Which Ip Do You Want To Scan :")
	os.system("nmap -v -sn %s" % (wep))

if op == '3' or op == '03':
	cls()
	logo()
	print "These Are Some Advanced Options From Nmap..."
	time.sleep(1)
	os.system("nmap")
	print "You Can use The By Typing 'Nmap <Option>'"
	time.sleep(2)
	sys.exit()

if op == '99':
	cls()
	logo()
	print "Sure! Quiting.... Hope U Liked"
	sys.exit()

if op == '4' or op == '04':
	cls()
	os.system("figlet -f slant About")
	print
	print "This Tools Is Made For The Newbie and Also Expert Hackers That Do Not Know How to use Nmap The Hacking Tools Because The Nmap has a Litle Difficul Statements To Exexute Them By This Tools You Do Not Have To Write  Any Statements You Can Exexute Nmap and Scan Websites By Just Writing The Name Of The Website/Ip Advanced Options are also there For Some Experts  "
	print""
	print "Author       -> Sarthak"
	print "Posted on    -> Github"
	print "Authors Age  -> 11 Years"
	print "Intrested in -> Cyber Security,Ethical Hacking,Tech"
	print ""

else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	sys.Exit()


		