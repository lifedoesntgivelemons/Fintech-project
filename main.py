# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:05:49 2020

@author: user
"""

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import stripe

app = Flask(__name__)
stripe_keys = {
  'secret_key': os.environ['STRIPE_SECRET_KEY'],
  'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

@app.route("/")
def home():
    return render_template("home.html")
#def home():
#    if not session.get('logged_in'):
#        return render_template('login.html')
#    else:
#        return "Hello!"
#@app.route('/login', methods=['POST'])
#def do_admin_login():
#    if request.form['password'] == 'password' and request.form['username'] == 'admin':
#        session['logged_in'] = True
#    else:
#        flash('wrong password!')
#    return home()
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/Transfer")
def Transfer():
    return render_template("Transfer.html", key=stripe_keys['publishable_key'])
@app.route('/charge', methods=['POST'])
def charge():

    # amount in cents
    amount = 500

    customer = stripe.Customer.create(
        email='first@customer.com',
        source=request.form['stripeToken']
    )

    stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description='Flask Charge'
    )

    return render_template('charge.html', amount=amount)
if __name__ == "__main__":
    app.run(debug=True)