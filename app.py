from flask import Flask, render_template

app = Flask(__name__) #Flask라는 class(F가 대문자로!)
@app.route('/')

def home():
    return render_template('index.html')


#페이지 추가
@app.route('/brand')
def menu1():
    return render_template('brand.html')


if __name__ == '__main__': 
    app.run(debug=True)  #자동으로 서버 재시작



