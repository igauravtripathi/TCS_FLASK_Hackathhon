from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,IntegerField,SubmitField,BooleanField,SelectField
from wtforms.validators import DataRequired, Email, Length,EqualTo,ValidationError


class LoginForm(FlaskForm):
    email= StringField("Email",validators=[DataRequired(),Email()])
    password= StringField("Password",validators=[DataRequired(),Length(min=6,max=15)])
    remember_me = BooleanField("Remeber Me")
    submit= SubmitField("Login")


class CreateCustomerForm(FlaskForm):
    Cityc = [('Mumbai', 'Mumbai'), ('Delhi', 'Delhi')]
    Statec = [('Maharasthtra', 'Maharasthtra'), ('Delhi', 'Delhi')]
    CustomerSSNID= StringField("Customer SSN ID",validators=[DataRequired(),Length(min=12)])
    Customer_name= StringField("Customer Name",validators=[DataRequired(),Length(min=4,max=15)])
    Age= StringField("Age",validators=[DataRequired(),Length(min=2)])
    Address= StringField("Address",validators=[DataRequired(),Length(min=2,max=55)])
    State =SelectField(u"State",choices=Statec)
    City= SelectField(u" City",choices=Cityc)
    submit= SubmitField("Submit")    
    reset= SubmitField("Reset")    
class UpdateCustomerForm(FlaskForm):
    Cityc = [('Mumbai', 'Mumbai'), ('Delhi', 'Delhi')]
    Statec = [('Maharasthtra', 'Maharasthtra'), ('Delhi', 'Delhi')]
    CustomerSSNID= StringField("Customer SSN ID",validators=[DataRequired(),Length(min=12)])
    Customer_name= StringField("Customer Name",validators=[DataRequired(),Length(min=4,max=15)])
    Age= StringField("Age",validators=[DataRequired(),Length(min=2)])
    Address= StringField("Address",validators=[DataRequired(),Length(min=2,max=55)])
    State =SelectField(u"State",choices=Statec)
    City= SelectField(u" City",choices=Cityc)
    submit= SubmitField("Update")    
      
    