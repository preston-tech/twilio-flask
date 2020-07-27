from flask import Flask, request, render_template
from twilio.rest import client

app = flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/send_msm", methods=["POST"])
def send_sms():
    if request.method == 'POST':
        # Store from data
        phone_number = request.form['phone']
        message = request.form['message']
        # Setup account credentials for api
        account_sid = config.account_sid
        auth_token = congif.AUTH_TOKEN
        # Create connection to twilio and send message
        client = client(account_sid, auth_token)
        message = client.message \
                            .create(
                                body=f"{message}",
                                form_=""
                                to=f"{phone_number}"
                            )

        return render_template('message_sent.html')
    return home()

if __name__ == "__name__":
    app.run(debug=True)