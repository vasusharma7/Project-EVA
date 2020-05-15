from flask import Flask, request, jsonify
from nmt_chatbot.inference import get_answers 
import random
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twitter import tweets
app = Flask(__name__)
admin = 'whatsapp:+919906330301'

sources = {"ht": "htTweets", "toi": "timesofindia",
           "ie": "IndianExpress", "dl": "DailyExcelsior1", "th": "the_hindu", "et": "EconomicTimes", "au": "HindiUjala"}

news_info = """Hi ,Welcome to VVS News Digest
You can type *#NH* for latest news

If you want news from a particular news source, see procedure below :

*#NH news_source*

News Sources Available Are:
Source                    TypeIn
Hindustan Times   :    ht
Times Of India       :    toi
Indian Express       :    ie
Daily Excelsior       :    dl
The Hindu             :     th
Amar Ujala            :     au
(Hindi)
Economic Times    :    et
(Default)

So type :
*#NH et*
*#NH ht*
*#NH dl*
etc....

If you want only 5 news headlines, you can type :
*#NH 5*
(Maximum 7 are allowed)

You can also do :
*#NH ht 7*

This will give latest 7 headlines from Hindustan Times

If you want this info again, send #news here
               """
last = ""               
@app.route('/', methods=['GET', 'POST'])

def test():

    return "Success"





@app.route('/response', methods=['GET', 'POST'])

def respond():
    data = request.args.get("question")
    data = data.lower()
    print(str(data))
    if data.lower() == "hi":
        return "Hi I am VVS Chatbot !!"
    response = get_answers(str(data))
    if response == "":
        return  "Sorry! I didn't quite get that "
    print(response)
    return jsonify({"answer" : response['answers'][response['scores'].index(max(response['scores']))],"score":max(response['scores'])})

@app.route("/check",methods=['GET','POST'])
def check():
    if last == 0:
        print(last)
        return "No response"
    resp = MessagingResponse()
    send = request.form.get("To")
    body = request.form.get("Body")
    print(send)
    body = "Hi!  I am a general purpose chatbot !"
    resp.message(
            to=send,
            body=body)
    print(resp)
    return str(resp)
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message

    resp = MessagingResponse()
    try:

        msg = request.form.get('Body')
        user = request.form.get('From')
        parts = msg.split('\n')
        trigger = msg[0]
        if msg.lower() == "hi":
           last = 1
        else:
            last  =0
        if "#news" == msg:
            body = news_info
            send = user
        elif "#NH" in msg or "#nh" in msg.lower():
            body = ""
            send = user
            msg = msg.split()
            if len(msg) == 1:
                num = random.randrange(1, 7)
                source = "EconomicTimes"
            elif len(msg) == 2:
                if msg[1].isnumeric():
                    num = int(msg[1])
                    source = "EconomicTimes"
                else:
                    num = random.randrange(1, 7)
                    source = msg[1].lower()
                    if source in sources.keys():
                        source = sources[source]
                    else:
                        body = news_info
                        source = ""
            else:
                num = int(msg[2])
                if num > 7:
                    num = 7
                source = msg[1].lower()
                if source in sources.keys():
                    source = sources[source]
                else:
                    body = news_info
                    source = ""
            if not source == "":
                newsBulk = tweets(num, source)
                print(newsBulk)
                for i, news in enumerate(newsBulk):
                    body += str(i + 1) + ". "
                    news = news.full_text
                    news = news.replace("#", "")
                    body += news
                    body += "\n"
                    body += "\n"
        elif user == admin and trigger.isnumeric():
            send = 'whatsapp:+91' + parts[0]
            if len(parts) == 1:
                body = "Hi there ! ✌\nYou are talking to Vasu's Personal Bot : Jarvis 😎\nTalk to me while Vasu is not unable to take up your messages/calls.😊"
            else:
                body = parts[1]
        else:
            msg = msg.lower()
            if msg == "hi":
                body = "Hi I am VVS Chatbot !!"
            else:
                response = get_answers(str(msg))
                if response == "":
                    body = "Sorry! I didn't quite get that"
                else:
                    print(response)
                    body = response['answers'][response['scores'].index(max(response['scores']))]

            send = user
        resp.message(
            to=send,
            body=body)
        print(resp)
        return str(resp)
    except:
        resp.message(
            to=admin,
            body='Some error occured : ' + user)
        print(resp)
        return str(resp)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=7000)
