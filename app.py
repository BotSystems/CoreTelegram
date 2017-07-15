from flask import Flask
from telegram.ext import Updater
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', True))
    appname = os.environ.get('APPNAME', 'NO-APP-NAME')
    token = os.environ.get('TOKEN', 'NO-TOKEN')
    return "{}:{}:{}:{}".format(port, debug, appname, token)

if __name__ == '__main__':
    schema = os.environ.get('SCHEMA')
    if schema not in ('longpooling', 'webhoos'):
        raise Exception('ALARMA')



    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', True))
    appname = os.environ.get('APPNAME', 'NO-APP-NAME')
    token = os.environ.get('TOKEN', 'NO-TOKEN')

    updater = Updater(token)
    updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
    updater.bot.set_webhook("https://{}.herokuapp.com/".format(appname) + token)
    updater.idle()

    app.run(host='0.0.0.0', port=port, debug=debug)
