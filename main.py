import ftp, ssh, telnet, portscan,auto
import time

def main(): # main 함수
    while True:
        print('********************************')
        print('< 취약 서버 공격용 모듈 >\n')
        print('1. 호스트 스캔 및 포트 스캔')
        print('2. telnet 공격')
        print('3. ssh 공격')
        print('4. ftp 공격')
        print('5. 자동 공격')
        print('6. 프로그램 종료')
        print('********************************')
        menu = input('메뉴를 입력하세요. ex) 1 : ')

        if menu == '1': # 호스트 스캔 및 포트 스캔
            try: #시도
                portscan.main()
            except: #오류 발생시
                print(' => 호스트 스캔 및 포트 스캔 중 오류가 발생하였습니다.')
        elif menu == '2': # telnet
            HOST = ''
            user = ''
            password = ''
            try: #시도
                telnet.main(HOST,user,password)
            except: #오류 발생시
                print(' => telnet 공격 실행 중 오류가 발생하였습니다.')
        elif menu == '3': # ssh
            server = ''
            user = ''
            password = ''
            passwdFile = ''
            try: #시도
                ssh.main(server,user,password,passwdFile)
            except: #오류 발생시
                print(' => ssh 공격 실행 중 오류가 발생하였습니다.')
        elif menu == '4': # ftp
            tgtHosts = ''
            passwdFile = ''
            try: #시도
                ftp.main(tgtHosts,passwdFile)
            except: #오류 발생시
                print(' => ftp 공격 실행 중 오류가 발생하였습니다.')
        elif menu == '5': # auto
            try: #시도
                auto.main()
            except: #오류 발생시
                print(' => 자동 공격 실행 중 오류가 발생하였습니다.')
        elif menu == '6': # exit
            print('\n3초 후에 프로그램을 종료합니다.')
            time.sleep(3) #3초 후
            return False

if __name__ == '__main__':
    main() # main 함수 실행
 