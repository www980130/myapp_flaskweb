from flask import Flask, render_template, request, redirect # flask 모듈 import
import pymysql

app = Flask(__name__) # __name__ 이라는 내장변수를 받아 새로운 instance인 app 생성
app.debug = True # 파일 저장할 때마다 서버 restart 하기 위해 debug 설정 추가

# database에 접근
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='agee04041**',
                     db='myapp',
                     charset='utf8')

# database를 사용하기 위한 cursor 세팅
cursor = db.cursor()

# root 페이지
@app.route('/', methods = ['GET', 'POST']) # @ : decorate
def main():
    return render_template("index.html")

# board 페이지
@app.route('/boards', methods=['GET', 'POST'])
def boards():
    sql = f"SELECT * FROM board_lists;" # SQL query 작성
    cursor.execute(sql) # SQL query 실행
    boards = cursor.fetchall() # boards는 tuple 안의 tuple 형태

    return render_template("board.html", data = boards)

# 게시글별 글 내용 보여주는 페이지
@app.route('/<idx>/board', methods=['GET', 'POST'])
def contents(idx):
    if request.method == "GET":
        sql = f"SELECT * FROM board_lists WHERE idx = {int(idx)};"
        cursor.execute(sql)
        board = cursor.fetchone() # fetchall 하면 indexing 2번 됨

        return render_template("detail.html", detail = board)

# 게시글 추가 페이지
@app.route('/board/add', methods=['GET', 'POST'])
def add_board():
    if request.method == 'GET':
        return render_template('add_board.html')
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        
        sql = f"INSERT INTO board_lists(title, content, author) VALUES('{title}', '{content}', '{author}');"
        cursor.execute(sql)
        db.commit() # 데이터 변화 적용

        return redirect('/boards')

# 게시글 삭제 페이지
@app.route('/<idx>/delete', methods=['GET'])
def del_board(idx):
    sql = f"DELETE FROM board_lists WHERE idx = {int(idx)};"
    cursor.execute(sql)
    db.commit()

    return redirect('/boards')

@app.route('/<idx>/edit', methods=['GET', 'POST'])
def edit_board(idx):
    if request.method == 'GET':
        sql = f"SELECT * FROM board_lists WHERE idx = {int(idx)};"
        cursor.execute(sql)
        board = cursor.fetchone()
        return render_template('edit_board.html', data = board)
    elif request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']

        sql = f"UPDATE board_lists SET title='{title}', content='{content}', author='{author}' WHERE idx = {int(idx)}"
        cursor.execute(sql)
        db.commit()

        return redirect('/boards')

if __name__ == '__main__':
    app.run(port = 3000)