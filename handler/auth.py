from tornado.web import RequestHandler
from pycket.session import SessionMixin
from model.account import User
import utils.auth
import time


class LoginHandler(RequestHandler, SessionMixin):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        if utils.auth.authentic(username, password):
            self.redirect('/')
            self.session.set('to_user', username)

        else:
            self.render('error.html')


class LogoutHandler(RequestHandler, SessionMixin):
    def get(self):
        pass


class RegistHandler(RequestHandler, SessionMixin):
    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_argument('username', '')
        password = self.get_argument('password', '')
        password_repeat = self.get_argument('password_repeate', '')
        # print(username, password_repeat, password)
        if(password == password_repeat):
            # 添加数据
            if utils.auth.register(username, password):
                self.render('register2.html')
            else:
                self.session.set('tudo_user', username)
                self.redirect('/')
        else:
            self.write('两次密码不匹配')