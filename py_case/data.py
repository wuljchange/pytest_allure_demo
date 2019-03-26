# 测试case
DATA = [
    ('测试两数相加', 10, 20, 30),
    ('测试两数相加', 10.0, 20, 'x type is not int')
]

DATA2 = [
    ('测试两数相减的绝对值', 10, 20, 15),
    ('测试两数相减的绝对值', 10, '2', 'y type is not int')
]

DATA3 = [
    ('测试替换掉字符串中的某些字符', '--hell -world++', ['-', '+'], 't', 'tthellotttworldtt')
]