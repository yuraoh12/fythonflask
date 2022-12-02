import pybo.models.db_util as db

def insert_user(user_dic) :
    sql = f'''
        INSERT INTO user(loginId, pass, username, sex, age, regDate)
        VALUES ('{user_dic['loginId']}', '{user_dic['passwd']}', '{user_dic['username']}',
        {user_dic['sex']}, {user_dic['age']}, NOW())  
    '''
    
    db.update(sql)

def get_user(loginId) :
    sql = f'''
        SELECT * 
        FROM user 
        WHERE loginId = '{loginId}'        
    '''
    return db.get_one(sql)    


def get_music_list() :
    sql = '''
        SELECT *
        FROM music 
    '''
    
    return db.get_list(sql)

def get_music(no) :
    sql =f'''
        SELECT *
        FROM music
        WHERE musicno = {no}
    '''
    
    return db.get_one(sql)

def insert_history(hist_param) :
    sql = f'''
        INSERT INTO history(userno, musicno, regDate) VALUES 
        ({hist_param['userno']}, {hist_param['musicno']}, NOW());
    '''    

    db.update(sql)