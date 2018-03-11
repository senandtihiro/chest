import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def serialize_instance(obj):
    d = {
        '__classname__': type(obj).__name__,
    }
    # print('hhhhhhhhh', vars(obj))
    # {'x': 2, 'y': 3}
    # vars()
    # 函数返回对象object的属性和属性值的字典对象。
    d.update(vars(obj))

    return d


classes = {
    'Point': Point
}


def unserialize_object(d):
    # print('d:', d)
    # print('type d:', type(d))

    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
        else:
            return d


def main():
    p = Point(2, 3)
    s = json.dumps(p, default=serialize_instance)
    # print(s)
    # 下面是反序列化，用来将一个字典还原为一个python对象
    a = json.loads(s, object_hook=unserialize_object)
    print(a)


if __name__ == '__main__':
    main()