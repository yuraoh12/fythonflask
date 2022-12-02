from flask import Blueprint, render_template, request, redirect, session
import pybo.models.sql_manager as db

bp = Blueprint('music', __name__, url_prefix='/music')

@bp.route('/list')
def music_list() :
    
    music_list = db.get_music_list()
    
    print(music_list)
    
    return render_template("list.html", music_list=music_list)

@bp.route('/play/<int:no>')
def play(no) :
    
    music = db.get_music(no)
    
    hist_param = {
        "userno" : session.get('loginUser')['userno'],
        "musicno" : no 
    }
    print(session.get('loginUser')) 
    db.insert_history(hist_param)
     
    return render_template("play.html", music=music)