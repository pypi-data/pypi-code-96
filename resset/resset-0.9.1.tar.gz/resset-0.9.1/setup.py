from setuptools import setup

setup(
    name='resset',# 需要打包的名字,即本模块要发布的名字
    version='v0.9.1',#版本
    description='A  module for test', # 简要描述
    py_modules=['ressetAPI',],   #  需要打包的模块
    author='zhangq', # 作者名
    author_email='569535175@qq.com',   # 作者邮件
    url='https://github.com/vfrtgb158/email', # 项目地址,一般是代码托管的网站
    # requires=['requests','urllib3'], # 依赖包,如果没有,可以不要
    license='MIT'
)