import getpass
import telnetlib

#HOST = "localhost"
def main(HOST,user,password):
    print('\n\n< telnet 공격을 시작합니다 >\n')
    if HOST =='': #HOST
        HOST = input("호스트 입력 : ")
    if user =='' or password =='': #user, password
        user = input('계정 입력 : ')
        password = getpass.getpass()
        try: #로그인 시도
            print(user,'/',password,'(으)로 로그인을 시도합니다. \n')
            tn = telnetlib.Telnet(HOST)
            tn.read_until(b"login: ")
            tn.write(user.encode('ascii') + b"\n")

            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(b"ls\n")
            tn.write(b"exit\n")

            print(tn.read_all().decode('ascii'))
        except: #오류 발생
            print(' => telnet 공격을 실패하였습니다. ')
    else: #user나 password가 있으면
        try: #로그인 시도
            print(user,'/',password,'(으)로 로그인을 시도합니다. \n')
            tn = telnetlib.Telnet(HOST)

            tn.read_until(b"login: ") #로그인
            tn.write(user.encode('ascii') + b"\n") #계정 입력

            if password: #패스워드가 있으면 입력
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.write(b"ls\n") #현재 위치 내 파일
            tn.write(b"exit\n") #telnet 종료

            print(tn.read_all().decode('ascii')) #telnet 로그인 시의 내용들 출력

        except: #로그인 오류 발생시
            print(' => telnet 공격을 실패하였습니다. ')

# if __name__ == '__main__':
#     main()
