
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime
import csv
import os

app = Flask(__name__)

# 세션 암호화 키
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")

# 관리자 계정
ADMIN_ID = os.environ.get("ADMIN_ID", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin1234")

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "responses.csv")

os.makedirs(DATA_DIR, exist_ok=True)


# 설문 페이지
@app.route("/")
def index():
    return render_template("index.html")


# 설문 제출
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    major = request.form.get("major", "").strip()
    ai_usage = request.form.get("ai_usage", "").strip()

    if not name or not major or not ai_usage:
        return "모든 항목을 입력해주세요.", 400

    with open(CSV_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            name,
            major,
            ai_usage
        ])

    return """
    <h2>설문 참여 완료</h2>
    <p>교육용 실습이 종료되었습니다.</p>
    <p>입력 데이터가 테스트 서버에 저장되었습니다.</p>
    <a href="/">메인 페이지로</a>
    """


# 관리자 로그인
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == ADMIN_ID and password == ADMIN_PASSWORD:
            session["admin_logged_in"] = True
            return redirect(url_for("admin"))

        return render_template("login.html", error="아이디 또는 비밀번호가 틀렸습니다.")

    return render_template("login.html")


# 관리자 페이지
@app.route("/admin")
def admin():
    if not session.get("admin_logged_in"):
        return redirect(url_for("admin_login"))

    responses = []

    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 4:
                    responses.append(row)

    responses.reverse()

    return render_template("admin.html", responses=responses)


# 관리자 로그아웃
@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
