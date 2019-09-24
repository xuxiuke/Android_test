# coding=utf-8


from test_interfacecase.bussiness.kernal_function import Kernal_function


class Login_logout(object):

    @staticmethod
    def login_logout():
        read_csv = Kernal_function('login/logout')
        return read_csv.sso_post_answer()["resultCode"]
