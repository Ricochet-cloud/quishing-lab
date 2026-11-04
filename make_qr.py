
import qrcode

# Flask 서버 주소
URL = "http://172.17.106.108:5000"  # QR코드에 연결할 Flask 서버 주소.(:5000은 Flask 기본 포트)

# QR코드 생성
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(URL)
qr.make(fit=True)

# 이미지 생성
img = qr.make_image(
    fill_color="black",
    back_color="white"
)

# PNG 저장
img.save("survey_qr.png")

print("QR코드 생성 완료!")
print(f"연결 주소: {URL}")
print("저장 파일: survey_qr.png")
