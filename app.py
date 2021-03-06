
# 开启循环，让服务一直等待请求的到来
import tornado.ioloop
# web 服务基本功能都封装在此模块中
import tornado.web
from tornado.web import RequestHandler
import tornado.options
from tornado.options import define, options
import tornado.httpserver
from handler import main, auth

# 指定默认端口
define('port', default=8000, help='run port', type=int)

# 相关配置及路由
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', main.IndexHandler),
            (r'/explore', main.ExploreHandler),
            # 动态传参
            (r'/post/(?P<post_id>\d+)', main.PostHandler),
            (r'/upload', main.UploadHandler),
            (r'/login', auth.LoginHandler),
            (r'/logout', auth.LogoutHandler),
            (r'/register', auth.RegistHandler),
        ]
        settings = dict(
            debug=True,
            # 模板静态文件配置
            template_path='templates',
            static_path='static',

            # 加密cookie
            cookie_secret='qwe123',
            # redis配置
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    # redis 第5个库
                    'db_sessions': 5,
                    'max_connections': 2 ** 30
                },
                'cookies': {
                    # 设置cookie过期时间
                    'expires_days': 30
                }
            }
        )
        super(Application, self).__init__(handlers, **settings)

app = Application()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    print('运行端口: ', options.port)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
