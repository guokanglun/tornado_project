from tornado.web import RequestHandler
from pycket.session import SessionMixin


class LoginHandler(RequestHandler, SessionMixin):
    def get(self):
        self.render('login.html')

    def post(self):
        pass


class LogoutHandler(RequestHandler):
    def get(self):
        pass


class RegistHandler(RequestHandler):
    def get(self):
        self.render('register.html')

    def post(self):
        pass