# QR코드 피싱(Quishing) 교육용 실습 프로젝트

## 1. 프로젝트 소개

대학생 설문조사 페이지를 활용하여 QR코드 기반 웹 접속 유도 과정을 이해하고, 웹 서버의 데이터 처리 및 저장 과정을 분석하기 위한 교육용 프로젝트입니다.

본 프로젝트는 보안 교육 및 허가된 테스트 환경에서 사용하는 것을 목적으로 합니다.

## 2. 개발 환경

- OS: Windows 11 / Kali Linux
- Language: Python
- Web Framework: Flask
- WSGI Server: Gunicorn
- Frontend: HTML / CSS
- Data Storage: CSV
- QR Generator: Python qrcode
- External Access: ngrok

## 3. 프로젝트 구조

quishing-lab/
├── app.py
├── make_qr.py
├── README.txt
├── .gitignore
├── data/
│   └── responses.csv
├── templates/
│   ├── index.html
│   ├── admin.html
│   └── login.html
└── .venv/

## 4. 주요 기능

### 설문 페이지
- 대학생 AI 활용 실태 설문
- 이름, 학과, AI 사용 빈도 입력
- Flask 서버로 설문 데이터 전송

### 데이터 저장
- 제출 시간 기록
- CSV 파일에 테스트 응답 저장

### 관리자 기능
- 관리자 로그인
- 관리자 전용 데이터 조회
- 총 제출 건수 확인
- 로그아웃

### QR코드 생성
- make_qr.py를 이용한 QR코드 PNG 생성
- 지정한 URL을 QR코드로 변환

## 5. Windows 실행 방법

프로젝트 폴더에서 실행합니다.

### 5-1. 라이브러리 설치

python -m pip install flask gunicorn "qrcode[pil]"

### 5-2. Flask 개발 서버 실행

python app.py

### 5-3. 브라우저 접속

설문 페이지:
http://127.0.0.1:5000

관리자 로그인:
http://127.0.0.1:5000/admin/login

※ Windows에서는 개발 및 테스트 목적으로 Flask 개발 서버를 사용할 수 있습니다.

## 6. Kali Linux 실행 방법

### 6-1. 필수 패키지 설치

sudo apt update
sudo apt install git gh python3 python3-venv python3-pip -y

### 6-2. GitHub Private 저장소 다운로드

GitHub CLI 로그인:

gh auth login

저장소 다운로드:

cd ~/Desktop
gh repo clone Ricochet-cloud/quishing-lab
cd quishing-lab

### 6-3. Python 가상환경 생성

python3 -m venv .venv

가상환경 활성화:

source .venv/bin/activate

### 6-4. 라이브러리 설치

pip install flask gunicorn "qrcode[pil]"

### 6-5. Gunicorn 서버 실행

gunicorn --bind 0.0.0.0:5000 app:app --workers 2

설문 페이지:
http://127.0.0.1:5000

관리자 로그인:
http://127.0.0.1:5000/admin/login

### 6-6. ngrok 실행

별도 터미널에서 실행:

ngrok http 5000

ngrok에서 제공하는 HTTPS 주소를 통해 외부 접속을 테스트합니다.

### 6-7. QR코드 생성

make_qr.py의 URL을 실제 ngrok HTTPS 주소로 변경합니다.

python3 make_qr.py

생성 파일:
survey_qr.png

이미지 확인:

xdg-open survey_qr.png

## 7. 주요 Linux 명령어 정리

### 프로젝트 폴더 이동

cd ~/Desktop/quishing-lab

### 가상환경 활성화

source .venv/bin/activate

### 가상환경 비활성화

deactivate

### Gunicorn 실행

gunicorn --bind 0.0.0.0:5000 app:app --workers 2

### Gunicorn 종료

Ctrl + C

### ngrok 실행

ngrok http 5000

### ngrok 종료

Ctrl + C

### 서버 연결 확인

curl -I http://127.0.0.1:5000

### 포트 상태 확인

ss -lntp | grep 5000

### CSV 데이터 확인

cat data/responses.csv

### QR코드 생성

python3 make_qr.py

### QR코드 이미지 열기

xdg-open survey_qr.png

## 8. 현재 진행 상황

[완료]
- Windows Flask 개발 환경 구축
- 설문 페이지 구현
- CSV 데이터 저장 기능
- 관리자 로그인 및 데이터 조회
- QR코드 생성 프로그램
- Windows 내부 기능 테스트
- Kali Linux 환경 이전 및 실행 검증
- Gunicorn 서버 실행 및 테스트
- ngrok 외부 접속 테스트
- QR코드 생성 및 설문 연동
- 외부 접속 설문 제출 및 CSV 저장 확인

[추후 진행]
- 실습 결과 및 서버 로그 분석
- QR코드 피싱 공격 과정 분석
- 보안 대응 방안 정리
- 실습 결과 보고서 작성

## 9. 보안 및 사용 안내

- 교육 및 허가된 테스트 환경에서만 사용합니다.
- 참여자에게 실습 목적과 데이터 수집 항목을 사전에 안내합니다.
- 실제 비밀번호, 인증 코드 및 민감한 개인정보를 수집하지 않습니다.
- 관리자 비밀번호와 Flask 세션 비밀 키는 외부에 공개하지 않습니다.
- 테스트 응답 데이터와 비밀 설정 파일은 GitHub에 업로드하지 않습니다.
- 관리자 페이지는 외부 공개 환경에서 별도의 접근 제한이 필요합니다.

## 10. 프로젝트 목적

QR코드 기반 피싱의 접속 유도 방식과 웹 서버의 데이터 처리 과정을 이해하고, 관련 보안 위협 및 예방·탐지 방안을 분석합니다.
