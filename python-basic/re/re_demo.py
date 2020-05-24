
import re

'''
正则表达式的符号和方法
    .: 点号，代表匹配任意字符，换行符\n除外
    *: 星号，匹配前面一个字符0次或者无限次
    ?: 问号，匹配前面一个字符0次或1次
    .*: 贪心算法
    .*?: 非贪心算法

    正则常用方法：
        findall: 匹配所有符合规律的内容，返回包含结果的列表
        search：匹配并提取第一个符合规律的内容，返回一个正则表达式对象
        sub：替换符合规律的内容，返回替换后的值

    常用技巧：

'''

secret_code="aksldfhlajxxIxxakljsdfhhajsdfxxLovexxglkjdfgakjdsfgkxxYouxxfgnadnfg"

#.号的使用 匹配任意字符，换行除外
a='xz123\n'
b= re.findall('x....',a)
print(b)
#\n换行无法匹配
b= re.findall('x......',a)
print(b)


