import razorpay
import json

from flask import Flask, render_template, request

app = Flask(__name__, static_folder="static", static_url_path='')
razorpay_client = razorpay.Client(auth=("<APP_ID>", "<APP_SECRET>"))


@app.route('/')
def app_create():
    data = {
        'amount': 5100,
        'currency': 'INR',
        'receipt': 'test receipt',
        'payment_capture': 1,
        'notes': {
            'key': 'value'
        }
    }

    order = razorpay_client.order.create(data)

    order_id = order['id']

    return render_template('app.html', order_id=order_id, amount=data['amount'])


@app.route('/charge', methods=['POST'])
def app_charge():
    params_dict = dict(request.form.iteritems())

    try:
        razorpay_client.utility.verify_payment_signature(params_dict)
    except ValueError:
        return json.dumps('Signature Validatioon failed')

    payment_id = request.form['razorpay_payment_id']

    return json.dumps(razorpay_client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.run()
