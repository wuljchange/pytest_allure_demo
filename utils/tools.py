import re


# test function demo
class TestNumberDemo:
    def __init__(self):
        pass

    @staticmethod
    def add(x: int, y: int):
        """
        测试两整数相加
        :return: 两数之和
        """
        if not isinstance(x, int):
            return 'x type is not int'
        if not isinstance(y, int):
            return 'y type is not int'
        return x+y

    @staticmethod
    def sub(x: int, y: int):
        """
        测试两整数相减
        :return: 差值的绝对值
        """
        if not isinstance(x, int):
            return 'x type is not int'
        if not isinstance(y, int):
            return 'y type is not int'
        return abs(x-y)


class TestStringDemo:
    def __init__(self):
        pass

    @staticmethod
    def replace_all(raw: str, pattern: list, new: str):
        """
        将文本字符串中的某些字符替换为目标字符
        :return:
        """
        if not isinstance(raw, str):
            return 'raw type is not str'
        if not isinstance(pattern, list):
            return 'pattern type is not list'
        if ' ' not in pattern:
            # 默认替换掉空格
            temp = re.sub(' ', new, raw)
            return re.sub(f"{pattern}", new, temp)
        return re.sub(f"{pattern}", new, raw)

    # def filter_left(self):
    #     """
    #     从左边开始替换掉字符串中不想要的字符，直到当前字符不满足过滤条件
    #     :return:
    #     """
    #     if not isinstance(self.s, str):
    #         return f'{self.s} type is not str'
    #     if not isinstance(self.pattern, str):
    #         return f'{self.pattern} type is not str'
    #     # 默认替换掉空格
    #     temp = self.s.lstrip()
    #     return temp.lstrip(self.pattern)


if __name__ == "__main__":
    s = 'hello world'
    s1 = s.replace(' ', '')
    s2 = re.sub('\s+', ' ', s)
    print(s2)