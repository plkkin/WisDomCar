from framework.basepage import BasePage


class LoginPage(BasePage):
    point_account = "//*[contains(text(),'请输入用户账户')]"
    error_login = 'body > div.el-message.el-message--error.is-closable'
    account_name = '请输入用户账户'
    password_name = '请输入密码'
    span_name = '#app > div > div > div > form > div.login-btn > button'  # 登录按钮 css
    order_menu = '#app > div > div.zd--index--head > div.head--left > img'  # 菜单按钮 css

    # 首页
    online_car_class = '.zd-colorAct'  # 在线警车 class
    track_query_class = '.zd-border'  # 轨迹查询 class
    unread_warning_text = "//*[text()='轨迹查询']"  # 未读预警 text

    # 轨迹查询
    inquire = '.zd-btn--color'  # 轨迹查询按钮
    locus_start_time = '/html/body/div[4]/div[2]/button[2]/span'
    locus_end_time = '/html/body/div[last()]/div[2]/button[2]/span'  # 使用last()  防止节点位置变化 取得最后一个节点




