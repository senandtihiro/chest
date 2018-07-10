import re

'''
准备工作（基础知识）
1，直接给出字符，精确的字符匹配
2，\d: 表示数字；\w: 表示字母
3, .： 可以匹配任何字符
4, *： 可以匹配任意个字符
5，+： 至少一个字符
6，？： 0个或者1个
7，{n}: 表示n个字符
8，{n, m}: 表示n到m个字符
9，[] : 中括号中的内容，是限制的字符范围，即只允许出现中括号中的字符
10：A|B: 表示A或者B
11，^: 表示开头 
12，$： 表示结尾
 

'''
def match_test():
    s = 'ABC\\-001'
    s = r'ABC\\-001'
    # match()方法判断是否匹配，若匹配，返回一个Match对象；若不匹配，返回None
    a = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    print(a is not None)
    b = re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
    print(b)

    test = '用户输入的字符串'
    if re.match(r'用户输入的字符串', test):
        print('ok')
    else:
        print('failed')


def split_test():
    s1 = 'a b   c'.split(' ')
    # 匹配连续的空格
    s2 = re.split(r'\s+', 'a b   c')
    # \s可以匹配空格， 加上中括号【 】+ 表示可以匹配一个以上， 逗号与空格顺序不限
    s3 = re.split(r'[\s\,]+', 'a,b, c  d')
    s4 = re.split(r'[\,\s]+', 'a,b, c  d')
    # 加入一个分号
    s5 = re.split(r'[\s\,\;]+', 'a,b;; c  d')
    print('s1, 空格分割: ', s1)
    print('s2: 连续空格分割', s2)
    print('s3: 空格加逗号分割', s3)
    print('s4: 逗号加空格分隔', s4)
    print('s4: 逗号加空格加分号分隔', s4)


def group_test():
    '''
    用正则表达式来提取字串的功能
    用()表示的就是要提取的分组（Group）
    ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
    :return:
    '''
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print('m: ', m)
    # group(0)永远是原始字符串
    r = m.group(0)
    print('原始字符串:', r)
    r1 = m.group(1)
    print('第一个字串:', r1)
    r2 = m.group(2)
    print('第二个字串:', r2)


def group_test_time():
    '''
    用于识别合法的时间
    :return:
    '''
    t = '19:05:30'
    m = re.match(
        r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
        t)
    r = m.groups()
    print('r: ', r)


def greedy_match_test():
    '''
    正则匹配默认是贪婪匹配
    :return:
    '''
    r = re.match(r'^(\d+)(0*)$', '102300').groups()
    print('贪婪匹配，只匹配到来开头：', r)
    # 如果想要阻止贪婪匹配，也就是尽可能少匹配
    # 加个?就可以 采用非贪婪匹配
    r2 = re.match(r'^(\d+?)(0*)$', '102300').groups()
    print('非贪婪匹配，可以匹配开头结尾：', r2)


def compile_test():
    '''
    编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
    用编译后的正则表达式去匹配字符串。
    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式
    :return:
    '''
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    print('预编译', re_telephone)
    print('预编译结果类型', type(re_telephone))
    r = re_telephone.match('010-12345').groups()
    # 直接匹配
    print('直接匹配', r)
    r2 = re_telephone.match('010-8086').groups()
    print('直接匹配', r2)


def is_valid_email(email_addr):
    m = re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$')


def main():
    # match_test()
    # split_test()
    # group_test()
    # group_test_time()
    # greedy_match_test()
    compile_test()

if __name__ == '__main__':
    main()