import webbrowser
import logging
from slack_sdk import WebClient
import threading
from flask import Flask, request
from werkzeug.serving import make_server
from PySide6.QtCore import Signal, QObject

from app.model.config_loader import Config
from app.model.static_globals import CLIENT_ID, CLIENT_SECRET, AUTH_URL, PRIVATE_TOKEN
from app.service.logger import logger


class AuthServer(threading.Thread, QObject):
    auth_server_received = Signal(object)

    def __init__(self):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        werkzeug_log = logging.getLogger('werkzeug')
        werkzeug_log.disabled = True
        self.logger = logger

        self.server = None
        self.thread = None
        self.timeout_timer = threading.Timer(60, self.stop_server)
        self.config = Config()

    def run(self) -> None:
        self.thread = threading.current_thread()
        self.logger.debug(f'Flask-listener server started on {self.thread}')
        app = Flask('server')
        app.logger.disabled = True
        webbrowser.open(self.config.get_app(AUTH_URL))

        self.timeout_timer.start()

        @app.route("/", methods=["GET", "POST"])
        def post_install():
            client = WebClient()
            response = {}
            if request.args.get('error'):
                self.auth_server_received.emit(None)
                return "<h1>Authorisation failed!<h1/>"

            slack_auth_code = request.args["code"]
            if slack_auth_code:
                response = client.oauth_v2_access(client_id=self.config.get_app(CLIENT_ID),
                                                  client_secret=self.config.get_app(CLIENT_SECRET),
                                                  code=slack_auth_code)
                self.config.update_user(PRIVATE_TOKEN, response.data.get('authed_user').get('access_token'))
            self.auth_server_received.emit(response.data)
            return "<h1>Authorisation complete!<h1/>"

        self.server = make_server('127.0.0.1', 5000, app, ssl_context='adhoc')
        ctx = app.app_context()
        ctx.push()
        self.server.serve_forever()

    def stop_server(self) -> None:
        if self.server:
            self.timeout_timer.cancel()
            self.server.shutdown()
        self.logger.debug(f'Flask-listener server stopped on {self.thread}')


if __name__ == '__main__':
    l = []
    serv = AuthServer()
    print(serv)
    print(serv.config)
    serv.start()
    l.append(serv)
    serv = AuthServer()
    print(serv)
    serv.start()
    l.append(serv)
    for i in l:
        i.stop_server()

