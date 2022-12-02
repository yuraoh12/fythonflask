import pymysql as my
import pybo.config.db_info as db_conf

host = db_conf.host
user = db_conf.user
password = db_conf.passwd
database = db_conf.db

# 커넥션 얻어오기
def get_connection() :
    conn = my.connect(host=host, user=user, password=password, database=database)
    return conn

# 커서 실행
def get_cursor(conn, sql) :
    cur = conn.cursor(my.cursors.DictCursor)    
    cur.execute(sql)
    return cur
    
# 한개 가져오기
def get_one(sql) :
    conn = get_connection()
    cur = get_cursor(conn, sql)
    return cur.fetchone()

# 여러개 가져오기
def get_list(sql) :
    conn = get_connection()
    cur = get_cursor(conn, sql)
    return cur.fetchall()

# 변경하기
def update(sql) :
    conn = get_connection()
    get_cursor(conn, sql)
    conn.commit()
