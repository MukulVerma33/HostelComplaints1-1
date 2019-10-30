from Levels import app, lm
from flask import request, redirect, render_template, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from Levels.forms import LoginForm, Registration, otpForm
from Levels.authenticate_model import Authenticate
from Levels.user.views import register
from Levels.user.views import sendConfirmationEmail


@app.route('/',methods=['GET', 'POST'])
def index():
    OTP = None
    form = Registration()
    form2 = LoginForm()
    form3 = otpForm()
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['rollno'] = form.rollno.data
        session['hostel'] = form.hostel.data
        session['roomno'] = form.roomno.data
        session['password'] = form.password.data
        session['contact'] = form.contact.data
        OTP = sendConfirmationEmail()
        session['OTP'] = OTP
        print(f"The OTP is {OTP}")
        # return redirect(url_for('index'))
    
    elif form2.validate_on_submit():
        session['email'] = form2.email.data
        session['password'] = form2.password.data
        return redirect(url_for('user.user_login'))

    elif form3.validate_on_submit():
        print(f'this is the received otp {form3.OTP.data} , {session["OTP"]}')
        if form3.OTP.data == session['OTP'] :
            register()
            session['OTP'] = None
        else:
            flash("Invalid OTP",'registerationProcess')
            flash("Invalid OTP",'invalidOTP')
    return render_template('index.html',form=form,form2=form2,form3=form3,OTP = OTP)
    
