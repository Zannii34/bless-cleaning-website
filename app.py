from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_this' 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/af')
def home_af():
    return render_template('af.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form.get('name')
    phone = request.form.get('phone')
    service = request.form.get('service')
    date = request.form.get('date')
    location = request.form.get('location')

    print(f"--- NEW BOOKING ---")
    print(f"Name: {name}\nPhone: {phone}\nService: {service}\nDate: {date}\nLocation: {location}")
    print(f"-------------------")

    flash(f"Thank you {name}! Your booking for {service} on {date} has been received. Bee will contact you shortly to confirm.", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)