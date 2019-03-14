#coding:utf8
import logging
from logging.handlers import RotatingFileHandler
#基本配置信息
class Config(object):

    DEBUG = True
    SECRET_KEY = "1221324"

    #数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@127.0.0.1:3306/userinformation"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #数据库内容发送改变之后,自动提交
    #SQLALCHEMY_ECHO=True
    #默认日志等级
    LEVEL = logging.DEBUG


#生产模式
class ProductConfig(object):
    DEBUG = False




#设置统一访问入口,使用config_dict
config_dict = {
    "config":Config,
    "product":ProductConfig
}

#日志文件,作用:用来记录程序的运行过程,比如:调试信息,接口访问信息,异常信息
def log_file(level):
    # 设置日志的记录等级,设置日志等级: 常见等级有:DEBUG < INFO < WARING < ERROR < FATAL(CRITICAL)
    logging.basicConfig(level=level)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件编号
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
