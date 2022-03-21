
from flask import Flask, render_template ,request,redirect,url_for, flash
from matplotlib.pyplot import bar_label
import app_module as m
app = Flask(__name__)
app.secret_key ="secret key" 
@ app.route('/')
def index():
        return render_template('index.html')
@ app.route('/signup' ,methods=['GET','POST'])
def signup():
        return render_template('signup.html')
@ app.route('/signupinsert',methods=['POST'])
def signupinsert():
    if request.method == 'POST':
            a=request.form['account']
            p=request.form['password']
            u= request.form['username']
            e=request.form['email']
            while True:
               if not m.sql_selectone(a) ==None:
                   flash("註冊失敗，此帳號: "+a+" 已被註冊!","danger") 
                   break
               m.sql_signupinsert(a,p,u,e)
               flash("已成功註冊會員:  "+a,"success")
               break
            return redirect(url_for('signup'))         
@ app.route('/login' ,methods=['GET','POST'])
def login():
        if request.method == 'GET':
             return render_template('login.html')
        if request.method == 'POST':
               a=request.form['account']
               p=request.form['password']
               while True:
                       actdata=m.sql_selectact(a)
                       pwddata=m.sql_selectpwd(p)
                       if not actdata ==None:
                               if not pwddata ==None:
                                       flash("已成功登入會員:  "+a,"success") 
                                       break
                               else:
                                       flash("密碼錯誤請重新輸入","warning") 
                                       break    
                       flash("帳號尚未註冊請先註冊帳號","danger")
                        
        

if __name__ == '__main__':
    app.run(debug=True)