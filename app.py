from bottle import run, route, template, request, response, redirect

adminuser = 'admin'
adminpwd = '12345'

@route('/')
def index():
    return template('index')

@route('/login')
def login():
    return template('login')

@route('/login', method='post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == adminuser and password == adminpwd:
        response.set_cookie('account', username, secret='my_secret_code')
        return redirect('/restricted')
    else:
        return "Login failed. <br> <a href='/login'>Login</a>"

@route('/restricted')
def restricted():
    user = request.get_cookie('account', secret='my_secret_code')
    print(user)
    if (user):
        return "Restricted area. <br> <a href='/signout'>log off</a>"
    else:
        return "You are not logged in. Access denied."

@route('/signout')
def signout():
    response.set_cookie('account', "", expires=0)
    return "You have been signed out. <br> <a href='/login'>Log in</a>"

run()
