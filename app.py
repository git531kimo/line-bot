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

line_bot_api = LineBotApi('wLFH60YyBJ2H4F9hQUknd2ST4V1lDS26fP/K3H8zHIyvSAh6Mdg44uowjSU3rM8/7tExvBqiFSZoN4wyf0iaz6hqax2jeYo26DCUFTUeB9FNE/NVBgcyaFn3v5K/Jf/E6lWgH73hvNeylBrpmSFHQwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('99484cc54588ef95715275fb13970ef0')


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
       # print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂'

    if mag in ['hi', 'Hi', 'HI']:
        r = 'hi'
    elif mag == '吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '你想訂什麼時候'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()