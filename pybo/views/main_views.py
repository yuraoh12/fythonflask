from flask import Blueprint, render_template, request
import pybo.models.sql_manager as db

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    
    #request.args['flag'] # 없으면 error
    #flag = request.args.get('flag') # 없으면 None
    #print(flag)
    #return render_template("main.html", flag=flag)
    return render_template("main.html")


@bp.route('/get_article')
def get_article():
    
    rs = db.get_article_list()    
    
    return "작업 완료"