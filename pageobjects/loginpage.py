from framework.basepage import BasePage


class LoginPage(BasePage):
    account_name = '请输入用户账户'
    password_name = '请输入密码'
    span_name = '#app > div > div > div > form > div.login-btn > button'  # 登录按钮 css
    menu = '#app > div > div.zd--index--head > div.head--left > img'  # 菜单按钮 css
