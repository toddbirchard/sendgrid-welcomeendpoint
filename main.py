import sys
import urllib.request as urllib
import json
import os
from flask import Flask, request, make_response
import sendgrid
from sendgrid.helpers.mail import Email, Content, Substitution, Mail


def welcome_mailer(request):
    """Send welcome email."""
    api_key = os.environ.get("SENDGRID_API_KEY")
    sg = sendgrid.SendGridAPIClient(apikey=api_key)
    if request.method == "POST":
        post_data = request.data
        data_dict = json.loads(post_data)
        print('data_dict = ', data_dict)
        sys.stdout.flush()
        subscribers = data_dict['subscribers']
        for subscriber in subscribers:
            to_email = Email(subscriber['email'])
            from_email = Email(os.environ["FROM_EMAIL"])
            subject = "Welcome to Hackers & Slackers"
            print("subscriber['email'] = ", subscriber['email'])
            sys.stdout.flush()
            mail = Mail(from_email, subject, to_email)
            mail.template_id = os.environ["TEMPLATE_ID"]
            try:
                response = sg.client.mail.send.post(request_body=mail.get())
                return make_response('it worked!', 200)
            except urllib.HTTPError as e:
                print(e.read())
                sys.stdout.flush()
                print(response.status_code)
                sys.stdout.flush()
                print(response.body)
                sys.stdout.flush()
                print(response.headers)
                sys.stdout.flush()
                return make_response(e.read(), 500)
    return make_response('Wrong method passed!', 400)
