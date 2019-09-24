# coding=utf-8

# 告诉编译器这是全局变量csv_dict
# global csv_dict
csv_dict = {}


def set_csv_dict_value(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global csv_dict
    csv_dict = value


def get_csv_dict_value():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global csv_dict
    return csv_dict


# 告诉编译器这是全局变量get_return
# global get_return
get_return = {}


def set_get_return_value(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global get_return
    get_return = value


def get_get_return_value():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global get_return
    return get_return


# 告诉编译器这是全局变量execute
# global execute
execute = ""


def set_execute_value(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global execute
    execute = value


def get_execute_value():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global execute
    return execute
