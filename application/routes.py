from application import app
from flask import Flask,flash,redirect,render_template,url_for,session,request,jsonify,json,Response
from application.forms import LoginForm,CreateCustomerForm,UpdateCustomerForm
@app.route('/')
@app.route('/index')
def index():
     if not session.get('username'):
        return redirect(url_for('login'))
    
     return  render_template('index.html',login=True)

@app.route('/Account',methods=['GET','POST'])
def Account():
    if session.get('username'):
        return redirect(url_for('index'))
    form=RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id +=1
        email =form.email.data
        password = form.password.data
        first_name =form.first_name.data
        last_name = form.last_name.data
        #user=User(user_id=user_id,first_name=first_name,last_name=last_name,email=email,password=password)
        #user.set_password(password)
        #user.save()
        flash("You are successfully registered","success")
        redirect(url_for('index'))
    return render_template('register.html',title="Register",form=form,register=True)

@app.route('/create_customer')
def create_customer():
    form =CreateCustomerForm()
    #if form.validate_on_submit():
    
    return render_template('create_customer.html',title='Create Customer Screen',form=form)   


@app.route('/update_customer')
def update_customer():
    form =UpdateCustomerForm()
    #if form.validate_on_submit():
    
    return render_template('update_customer.html',title='Update Customer',form=form) 


@app.route('/Operation')
def Operation(term="2019"):
    pass
@app.route('/login',methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form= LoginForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        password =request.form.get("password")
        #user=User.objects(email=email).first() 
        user="demo@demo.com" 
        passwords="123456"
        if email==user and password ==passwords:
            flash("You successfully logged in!","success")
            session['user_id']=passwords
            session['username']=user
            return redirect('/index')
        else:
            flash("Sorry, Something went wrong!","danger")
    return render_template('login.html',title="Login",form=form,login=True)
@app.route('/logout')
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect('/login')   
@app.route('/Status',methods=['GET','POST'])
def Status():
    id=request.form['courseID']
    title=request.form['title']
    term=request.form['term']
    return render_template('enrollment.html',enrollment=True, data={"id":id,"title":title,"term":term})

@app.route('/api')
@app.route("/api/<idx>")
def api(idx=None):
    if idx==None:
        jdata=cdata
    else:
        jdata=cdata[int(idx)]    
        
    return Response(json.dumps(jdata),mimetype="application/json")



@app.route("/user")
def user():
    #User(user_id=1,first_name="Gaurav",last_name="Tripathi",email="demo@demo.com",password="1234567").save()    
    #User(user_id=2cd,first_name="Saurabh",last_name="Yadav",email="demo@demo.com",password="1234567").save()
    #users= User.objects.all()
    return render_template("user.html",users=users)    


