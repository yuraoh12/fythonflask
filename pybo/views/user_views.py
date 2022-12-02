from flask import Blueprint, render_template, request, redirect, session
import pybo.models.sql_manager as db

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/showForm')
def show_form() :
    return render_template("form.html")

@bp.route('/addUser')
def add_user() :
    
    login_id = request.args['loginId']
    passwd = request.args['pass']
    username = request.args['username']
    sex = request.args['sex']
    age = request.args['age']
    
    user_dic = {
        "loginId" : login_id,
        "passwd" : passwd,
        "username" : username,
        "sex" : sex,
        "age" : age
    }
    
    db.insert_user(user_dic)
    
    return redirect('/?flag=1')

@bp.route('/loginForm')
def login_form() :
    return render_template('login_form.html')

@bp.route('/logout')
def logout() :
    session.pop("loginUser", None)
    return redirect('/')

@bp.route('/loginCheck')
def login_check() :
    
    # 아이디
    loginId = request.args.get("loginId")
    # 비밀번호   
    passwd = request.args.get("pass")
    
    target = db.get_user(loginId)
    
    if target == None :
        return "없는 회원입니다."
    
    if target["pass"] != passwd :
        return "비밀번호를 틀렸습니다."
    
    session['loginUser'] = target
        
    # return f"로그인 성공! {target['username']}님 반갑습니다."
    return render_template('main.html')

@bp.route('/param')
def param_test() :

    data1 = request.args.get('data1')
    print(data1)
    data2 = request.args.get('data2')
    print(data2)
    
    return "작업완료"
    
    