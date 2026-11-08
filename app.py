from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_this' # Needed for flash messages

# --- ROUTES ---
@app.route('/')
def home():
    # Renders the English homepage
    return render_template('index.html')

@app.route('/af')
def home_af():
    # Renders the Afrikaans homepage
    return render_template('af.html')

# --- GOOGLE VERIFICATION ROUTE ---
@app.route('/googleacc48534b94160a1.html')
def google_verify():
    # Serves the verification file directly from the static folder to the root URL
    return send_from_directory('static', 'googleacc48534b94160a1.html')

@app.route('/book', methods=['POST'])
def book():
    # This grabs the data from the booking form
    name = request.form.get('name')
    phone = request.form.get('phone')
    service = request.form.get('service')
    date = request.form.get('date')
    location = request.form.get('location')

    # --- HERE IS WHERE YOU WOULD SEND AN EMAIL OR SAVE TO DATABASE ---
    # For now, it will just print to the terminal and show a success message.
    print(f"--- NEW BOOKING ---")
    print(f"Name: {name}\nPhone: {phone}\nService: {service}\nDate: {date}\nLocation: {location}")
    print(f"-------------------")

    # Show success message on the website
    flash(f"Thank you {name}! Your booking for {service} on {date} has been received. Bee will contact you shortly to confirm.", "success")
    
    # Redirect back to the homepage
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Runs the app on http://127.0.0.1:5000
    app.run(debug=True, port=5000)
