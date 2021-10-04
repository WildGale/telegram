from flask import *
import requests
app = Flask(__name__)

@app.route('/tradingview', methods=['GET', 'POST'])
def home():
	json_data = request.json
	symbol = str(json_data["symbol"])
	price = str(json_data["price"])
	message = symbol + " Long " + price
	telegram_bot_sendtext(message)
	return message

def telegram_bot_sendtext(bot_message):

    bot_token = '2029480345:AAHwiJkt-cbQJy8_NSaFvu3A75SDoNX3_uA'
    bot_chatID = '362080911'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                '&parse_mode=Markdown&text=' + bot_message

    requests.get(send_text)

if __name__ == "__main__":
	app.run(debug=True)