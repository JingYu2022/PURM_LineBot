from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('y/MZH3Lo/u1qOwAQ8vBYT8haynKsOE2/d+CUTu0uQiFAQA4E0fmywb79d6O8nA5oiAwGE1SsCOaQJ5xqo+qPF0wCpddvxIwXbSr7BYQgUq9cV8f5dtRDrtJK8EXRMT9ijhgkpdhx5TKJhBeKpuT/3wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1501dde645084c1eece1cc4d96b40cf8')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
