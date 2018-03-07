def _update_content(content):
    '''
    更新前:
    "稍安勿躁，微调{{TTS_py|tags('tiao2')}}一下效果更好哦",
    更新后:
    "稍安勿躁，微{{TTS_pyt|tags('tiao2')}}调一下效果更好哦",
    :param content:
    :return:
    '''
    str = '{{TTS_py|tags('
    start_indexs = [i for i in range(len(content)) if content.startswith(str, i)]
    mapped_end_indexs = [content[index + 1:].find('}}') + index + 3 for index in start_indexs]
    tags = []
    replaces = []
    for i in range(len(start_indexs)):
        start_index = start_indexs[i]
        end_index = mapped_end_indexs[i]
        tag_str = content[start_index: end_index]
        if tag_str in tags:
            continue
        else:
            tags.append(tag_str)
            cn_char = content[start_index - 1: start_index]
            old_str = cn_char + tag_str
            new_str = tag_str + cn_char
            replaces.append((old_str, new_str))

    for old_str, new_str in replaces:
        content = content.replace(old_str, new_str)

    return content


def main():
    content = "稍安勿躁，微调{{TTS_py|tags('tiao2')}}一下效果更好哦"
    new_content = _update_content(content)
    print(new_content)


if __name__ == '__main__':
    main()