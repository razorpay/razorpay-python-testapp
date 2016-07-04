import razorpay
import json

from flask import Flask, render_template, request

app = Flask(__name__,static_folder = "static", static_url_path='')
razorpay_client = razorpay.Client(auth=("<APP_ID>", "<APP_SECRET>"))


@app.route('/')
def app_create():
    return render_template('app.html')


@app.route('/charge', methods=['POST'])
def app_charge():
    amount = 5100
    payment_id = request.form['razorpay_payment_id']
    razorpay_client.payment.capture(payment_id, amount)
    return json.dumps(razorpay_client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.run()
