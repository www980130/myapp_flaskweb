from flask import Flask, render_template, request # flask 모듈 import
from data import Boards #모듈 형식으로 data.py의 articles 가져오기

app = Flask(__name__) # __name__ 이라는 내장변수를 받아 새로운 instance인 app 생성
app.debug = True # 파일 저장할 때마다 서버 restart 하기 위해 debug 설정 추가

# root 페이지
@app.route('/', methods = ['GET', 'POST']) # @ : decorate
def main():
    return render_template("index.html")

# board 페이지
@app.route('/boards', methods=['GET', 'POST'])
def boards():
    board = Boards() # boards는 리스트 형태
    return render_template("board.html", data = board)

# 게시글별 글 내용 보여주는 페이지
@app.route('/<index>/board', methods=['GET', 'POST'])
def contents(index):
    if request.method == "GET":
        board = Boards()
        return render_template("detail.html", detail = board[int(index)-1])

if __name__ == '__main__':
    app.run(port = 3000)