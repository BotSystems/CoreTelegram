from flask import Flask
from telegram.ext import Updater
import os
from os.path import join, dirname
from longpoling.run import main as run_lognpooling
from webhook.run import main as run_webhook
from dotenv import load_dotenv

app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def index():
    # port = int(os.environ.get('PORT', 5000))
    # debug = bool(os.environ.get('DEBUG', True))
    # appname = os.environ.get('APPNAME', 'NO-APP-NAME')
    # token = os.environ.get('TOKEN', 'NO-TOKEN')
    # return 'ok'
    # return "{}:{}:{}:{}".format(port, debug, appname, token)

@app.route("/", methods=['GET', 'POST'])
def landing():
    return 'ok'

if __name__ == '__main__':
    # Prepare data
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    # Run longpooling mode
    if os.getenv('SCHEMA') == 'longpooling':
        data = {
            'token': os.getenv('TOKEN', 'NO-TOKEN')
        }
        run_lognpooling(data)
    # Run webhook mode
    elif os.getenv('SCHEMA') == 'webhook':
        data = {
            'token': os.getenv('TOKEN'),
            'appname': os.getenv('APPNAME'),
            'port': os.getenv('PORT'),
            'debug': os.getenv('DEBUG')
        }
        run_webhook(data)
    else:
        raise Exception('ALARMA! SCHEMA NOT VALID!')



    # port = int(os.environ.get('PORT', 5000))
    # debug = bool(os.environ.get('DEBUG', True))
    # appname = os.environ.get('APPNAME', 'NO-APP-NAME')
    # token = os.environ.get('TOKEN', 'NO-TOKEN')

    # updater = Updater(token)
    # updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
    # updater.bot.set_webhook("https://{}.herokuapp.com/".format(appname) + token)
    # updater.idle()

    # app.run(host='0.0.0.0', port=port, debug=debug)
