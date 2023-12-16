#MOGA DER IP UNBLOCKER🤣

import os,time,requests
#----------[basic colors]----------#
green="\033[1;32m";red="\033[1;31m";reset="\033[0m"
#----------[main logo]----------#
def logo():
 os.system("clear");print(f'''{reset} ╦╔═╗  ╦ ╦┌┐┌┬  ┌─┐┌─┐┬┌─
 {red}║╠═╝  ║ ║││││  │ ││  ├┴┐{reset}
 ╩╩    ╚═╝┘└┘┴─┘└─┘└─┘┴ ┴

 Author  : TOR NANIR HAU*_YA*
 About   : FUCK YOUR GF
{50 * '-'}''')
def ip():
 ip = requests.get("https://api.ipify.org").text
 logo()
 print(f"\n [{red}•{reset}] USE AIRPLANE MODE FOR 5 SEC BEFORE USE . ") 
 input(f" [{red}•{reset}] PRESS ENTER TO START ... ") 
 print(50*'\033[1;97m-')
 print(f" [{red}•{reset}] FINDING YOUR FUCKING IP ADDRESS ... ");time.sleep(3)
 print(f" [{red}•{reset}]{green} YOUR FUCKING IP ADDRESS : {ip} ")
 print(f" {reset}[{red}•{reset}]{green} TRYING TO UNBLOCK YOUR FUCKING IP ... ");time.sleep(3)
 print(f" {reset}[{green}✓{reset}]{green} YOUR FUCKING IP UNBLOCK SUCCESSFULLY☺️ \n\n ")
 print(f" AKON JAIYE HOGAR CLONNING KORA GA,BIDAY")
 exit() 
ip()