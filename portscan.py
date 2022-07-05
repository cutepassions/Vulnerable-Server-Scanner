#!/usr/bin/env python3

from datetime import datetime
import ipaddress
import socket
import os

def main():
	tgtHosts = {}
	
	ports = {21:'ftp', 22:'ssh', 23:'telnet'} #포트 리스트

	ip_range = input('\n\n호스트 입력 (10.10.10.4-5 가능) : ') #ip입력
	if '-' not in ip_range:
		ip_range1 = ip_range.split('.')[:-1] #ip대역대
		ip_range2 = ip_range.split('.')[-1] #시작 ip범위
		ip_range3 = ip_range.split('-')[-1]
	else:
		ip_range1 = ip_range.split('.')[:-1] #ip대역대
		ip_range2 = ip_range.split('-')[0].split('.')[-1] #시작 ip
		ip_range3 = ip_range.split('-')[-1] #마지막 ip

	ip = ''
	for i in ip_range1:
		ip += i + '.'


	if '-' in ip_range:
		ip_range = []
		for i in range(int(ip_range2),int(ip_range3)+1):
			ip_range.append(ip+str(i))
	else:
		ip_range = []
		ip_range.append(ip_range3)

	start_time = datetime.now() #현재 시각
	print('\n< 호스트 스캔 및 포트 스캔을 시작합니다 >')
	for host in ip_range:
		timelog = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #현재시각
		print('\n'+timelog + " : " + str(host)+ '(으)로 스캔 시도중')
		alive = os.system("ping -c 1 " + str(host) + " > /dev/null") #핑 보내기
		if alive == 0: #살아있으면
			print(' - '+str(host) + " is up")
			test = []
			for port in ports: #포트 스캔
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 생성
				result = sock.connect_ex((str(host), port)) #소켓 연결
				if result == 0: #살아있으면
					test.append(ports[port])
					print(' - [+] '+str(port) + "번 포트 열려 있음") #출력
				sock.close() #소켓 닫기
			tgtHosts[host] = test
		else: #죽어있으면
			print(str(host) + " is down")

	end_time = datetime.now() #끝난 시각

	print("\n스캔 걸린 시간 : " + str(end_time - start_time)+'\n') #걸린 시간

	return tgtHosts

# if __name__ == '__main__':
# 	main()