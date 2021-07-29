from flask import Flask # flask 모듈 import

app = Flask(__name__) # __name__ 이라는 내장변수를 받아 새로운 instance인 app 생성
app.debug = True # 파일 저장할 때마다 서버 restart 하기 위해 debug 설정 추가

@app.route('/', methods = ['GET', 'POST']) # @ : decorate
def main():
    return "This is a main page"

if __name__ == '__main__':
    app.run(port = 3000)