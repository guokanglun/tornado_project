import hashlib
from model.account import User

# 注册
def register(username, passsword):
    # 判断用户名是否存在，存在表示已经注册
    if(User.is_exits(username)):
        return True
    else:
        passsword = hashlib.md5(passsword.encode()).hexdigest()
        User.add_user(username, passsword) 

# 登录认证
def authentic(username, password):
    if(hashlib.md5(password.encode()).hexdigest() == User.get_password(username)):
        return True
    else:
        return False