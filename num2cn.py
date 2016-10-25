def contains_none_0(list):
    for i in range(len(list)):
        if list[i] != '0':
            return True
    return False


def number2dx(str):
    num_list_dx = ['零', '一', '二', '三',  '四', '五', '六', '七', '八', '九']
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_dict = {}
    # 将阿拉伯数字跟汉字对应起来构成字典
    for k, v in zip(num_list, num_list_dx):
        num_dict[k] = v
    # print('num_dict:', num_dict)
    res = []
    length = len(str)
    if length < 5:
        qz_list = ['千', '百', '十', '']
    elif 5 <= length < 9:
        qz_list = ['千', '百', '十', '万', '千', '百', '十', '']
    elif 9 <= length < 13:
        qz_list = ['千', '百', '十', '兆', '千', '百', '十', '万', '千', '百', '十', '']
    leng_of_qz = len(qz_list)
    for i in range(length):
        char = str[i]
        # 如果0在中间
        if char == '0' and str[i+1] == '0' and contains_none_0(str[i+1:]):
            print('1')
            continue
        elif char == '0' and str[i+1] != '0':
            res += num_dict[char]
        # 如果0全在末尾
        elif char == '0' and contains_none_0(str[i+1:]) == False:
            break
        else:
            res += num_dict[char] + qz_list[leng_of_qz-length+i]
    # 最后将列表转化为字符串
    return ''.join(res)


def main():
    while True:
        number = input('请输入要转化的数字：')
        print(number2dx(number))


if __name__ == '__main__':
    main()


'''
本次程序总结：
先考虑最简单的情况 不包含0且位数为四位之内的数，位数多了之后再做进一步修正
观察各种情况之下不变的东西是什么
最后考虑优化
'''