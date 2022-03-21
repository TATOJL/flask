import pymysql
#==================================================
def sql_read():
    # Connect to the database
    # create a pymysql.connect object 'conn'
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')

    #with conn session 
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
            # 使用 cur.execute() 執行select sql script
            sql = "select member_id,account, password,identity_type, username,email, \
                DATE_FORMAT(date, '%Y-%m-%d %T') \
                from `member`"
            cur.execute(sql)
            #使用 cur.fetchall() 從cur中取出資料
            #return value 'rows' --> tuple of tuples
            rows=cur.fetchall() 
    # conn is not autocommit by default. So you must commit to save your changes.
        conn.commit()
    return list(rows)
# define function sql_delete()
def sql_delete(accountdata):
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
            # Create a new record
            sql = "DELETE FROM `member` where `account` = %s"
            cur.execute(sql, (accountdata))
    # conn is not autocommit by default. So you must commit to save your changes.
        conn.commit()                             

def sql_update(account,password,username,email,identity_type,accountdata):
    # Connect to the database
    # create a pymysql.connect object 'conn'
    conn = pymysql.connect(host='localhost',
                                 
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')

    #with conn session 
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
            sql = "UPDATE `member` SET `account`=%s, `password`=%s, `username`=%s,\
                `email`=%s ,`identity_type`=%s WHERE `account`= %s"
            #print(sql) #test sql string
            cur.execute(sql, (account,password,username,email,identity_type,accountdata))
    # conn is not autocommit by default. So you must commit to save your changes.
        conn.commit()



#define function sql_insert()
def sql_insert(account, password,  username,email,identity_type):
    # Connect to the database
    # create a pymysql.connect object 'conn'
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')

    #with conn session 
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
            # Create a new record
            sql = "INSERT INTO `member` (`account`, `password`, `username`,\
                `email`, `date`,`identity_type`) VALUES (%s, %s, %s, %s, NOW(),%s)"
            cur.execute(sql, (account, password,username, email,identity_type))
    # conn is not autocommit by default. So you must commit to save your changes.
        conn.commit()

def sql_signupinsert(account, password,  username,email):
    # Connect to the database
    # create a pymysql.connect object 'conn'
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')

    #with conn session 
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
            # Create a new record
            sql = "INSERT INTO `member` (`account`, `password`, `username`,\
                `email`, `date`) VALUES (%s, %s, %s, %s, NOW())"
            cur.execute(sql, (account, password,username, email))
    # conn is not autocommit by default. So you must commit to save your changes.
        conn.commit()
def sql_selectone(account):
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')

    #with conn session 
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
           sql="SELECT * FROM `member` WHERE `account` = '"+ account +"'"
           cur.execute(sql)
           data=cur.fetchone()
           return data

def sql_search(account):
    conn = pymysql.connect(host='localhost',
                                 user='root',
                                 password='kjh123efr',
                                 database='aiweb',
                                 charset='utf8mb4')

    #with conn session 
    with conn:
        #with conn.cur object cur session
        with conn.cursor() as cur:
           sql="SELECT * FROM `member` WHERE `account` = '"+ account +"'"
           cur.execute(sql)
           data=cur.fetchall()
           return data
#=================================================
