# Vulnerable-Server-Scanner (취약 서버 스캐너)
## 프로젝트 개요
### 목표
- 파이썬을 이용하여 취약 서버의 호스트에 대해서 스캔 후 서비스별 공격 시도   
### 사용 스킬
- Python(3.6.8)   
### 사용된 파이썬 라이브러리
- time, ftplib, datetime, socket, os, paramiko, logging, getpass, telnetlib  
### 사용 환경
- Centos7

### 기능
- 호스트 및 포트 스캔
- telnet 공격
- ssh 공격
- ftp 공격
- 자동 공격 (위의 기능들을 통합해서 자동으로 실행)
- 프로그램 종료

## 메인 화면
- 메뉴들을 보여줌

![image](https://user-images.githubusercontent.com/105566077/177364265-1c8dd097-fe7e-4af7-9732-b093538e5ee4.png)   
=> python main.py 명령어를 통해서 메인 프로그램 실행   
=> 이후 메뉴 번호를 입력해서 해당 기능들 실행

## 호스트 및 포트 스캔
- 호스트를 입력하고 21, 22, 23번 포트가 열려있는지 확인

![image](https://user-images.githubusercontent.com/105566077/177365705-35b22e46-4dc2-4f8b-8471-60d57e675b3f.png)   
=> 단일 호스트 혹은 호스트 범위를 입력해서 해당 호스트(들)에 대해서 포트 스캔

## telnet 공격
- telnet으로 해당 호스트에 로그인

![image](https://user-images.githubusercontent.com/105566077/177366267-9fb9f025-40cc-4f01-992f-700d4b9bcd39.png)   
![image](https://user-images.githubusercontent.com/105566077/177366654-79539654-001f-4ec6-b358-d65cc7f61f92.png)   
=> 사용자에게 입력받은 계정으로 접속하여 특정 명령어를 입력한 후에 이후 접속 종료   

## ssh 공격
- ssh로 해당 호스트에 로그인

![image](https://user-images.githubusercontent.com/105566077/177367987-4f27f881-f6e1-43ac-a8cd-d9b3ac4feab4.png)   
=> 호스트를 입력하고 딕셔너리 공격을 위한 텍스트 파일을 입력하면 공격 시작

![image](https://user-images.githubusercontent.com/105566077/177368169-ce5bbb75-43af-4458-bc66-2c8bb26b0d5f.png)
(userpass.txt)   
=> 콜론의 앞은 ID, 뒤는 PW

## ftp 공격
- ftp로 해당 호스트에 로그인 한 뒤 악성 페이지를 업로드하여 해당 호스트의 웹 사이트 공격

![image](https://user-images.githubusercontent.com/105566077/177369175-c2771704-5bda-4411-aed2-95e5cded6618.png)   
=> Anonymous 로그인 가능 여부 확인   
=> 이후 딕셔너리 공격을 위해 텍스트 파일 입력   
=> 로그인 성공 시 해당 계정의 웹 서버 폴더로 이동한 후 공격 페이지를 업로드   
![image](https://user-images.githubusercontent.com/105566077/177374208-f430ebce-0580-4314-ada4-4b8f030e894e.png)   
![image](https://user-images.githubusercontent.com/105566077/177371170-a9188e2c-c756-42c4-824f-5f8fec0183d1.png)   
공격 전 페이지   
![image](https://user-images.githubusercontent.com/105566077/177372891-bca0d884-a729-4edd-92e0-ed55d19c5acc.png)   
공격 이후 페이지   

=> 페이지 접속 시 경고 메시지   

=> 지금은 경고 메시지만 표출했지만 해커가 악성 스크립트를 삽입하여 해킹가능

## 자동 공격
- 자동 공격은 위의 기능들을 하나의 기능으로 통합하여 호스트 스캔부터 ftp공격까지 한 번에 수행

![image](https://user-images.githubusercontent.com/105566077/177379397-e93504e9-efd8-4f7c-befc-e9ccbdb9657f.png)   
=> 입력받은 호스트(들)에 대해서 스캔 후 공격 가능한 서비스를 리턴받아 이를 표출   
=> 공격 여부 및 딕셔너리 공격을 위한 텍스트 파일 입력
=> 이후 서비스들에 대해서 ftp > ssh > telnet 순으로 공격 시도   
=> 해당 과정에서 ftp및 ssh를 딕서너리 공격으로 공격을 시도하고 로그인 성공 시 해당 계정을 기반으로 이후 서비스들을 공격   
=> 공격 완료 후 공격 완료 메시지 출력   
![image](https://user-images.githubusercontent.com/105566077/177380344-c8092a39-3ba9-4d9b-95da-d6e3b7fa2673.png)


## 프로젝트 결과
### 소요 기간
- 1.5개월
### 아쉬운 점
1. telnet 공격 시도시 딕셔너리 공격으로 하려고 했으나, telnet 라이브러리를 사용하여 로그인을 시도하면 한 번 로그인 실패시 1분 가량을 기다려야해서 딕셔너리 공격을 사용하면 너무 많은 시간이 소요 된다.
2. 현재는 직접 파이썬 프로그램을 실행하여 CLI 창에서만 구동이 가능하나, 이를 웹으로 이동시켜 웹 상에서 GUI 환경으로 구동을 하고 싶었다.
### 느낀 점
- python의 여러 라이브러리를 통해서 취약 서버 스캐너를 만들어 서버에 공격도 해보고 하는 것이 재미있었다.
