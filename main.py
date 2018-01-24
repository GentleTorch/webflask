
from flask import Flask,request,make_response,redirect,abort,render_template

app=Flask(__name__)

@app.route('/')
def index():
    user_agent=request.headers.get('User-Agent')

    response=make_response('<h1>This doc carries a cookies</h1>')
    response.set_cookie('answer','42')
    #return response

    return render_template('index.html')

    #return redirect('http://www.baidu.com')

   # return '<h1>hello world</h1>'+'<br><p>Your browser is %s</p></br>'%user_agent

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.route('/user/<id>')
def get_user(id):
    user=load_user(id)
    if not user:
        abort(404)
    return '<h1>hello %s</h1>'%user.name


if __name__=='__main__':
    app.run(debug=True)

