# from flask import Flask
# from telegram.ext import Updater
# import os
# from os.path import join, dirname


# from dotenv import load_dotenv
# import sys

# app = Flask(__name__)

# @app.route("/landing", methods=['GET', 'POST'])
# def landing():
#     return 'ok'

# if __name__ == '__main__':
#     # Prepare data
#     dotenv_path = join(dirname(__file__), '.env.bleat')
#     load_dotenv(dotenv_path)

#     # Run longpooling mode
#     if os.getenv('SCHEMA') == 'longpooling':
#         from longpoling.run import main as run_lognpooling
#         data = {
#             'token': os.getenv('TOKEN', 'NO-TOKEN')
#         }
#         run_lognpooling(data)
#     # Run webhook mode
#     elif os.getenv('SCHEMA') == 'webhook':
#         from webhook.run import main as run_webhook
#         data = {
#             'token': os.getenv('TOKEN'),
#             'appname': os.getenv('APPNAME'),
#             'port': os.getenv('PORT'),
#             'debug': os.getenv('DEBUG')
#         }
#         run_webhook(data)
#     else:
#         raise Exception('ALARMA! SCHEMA NOT VALID!')


