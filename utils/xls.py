import json
import pathlib
from tablib import Databook

HOMEPATH = pathlib.Path(__file__).parent.parent


# 解析xls文件的case
def gen_xls_data(book_name, sheet_name):
    book_name += '.xls'
    book_path = HOMEPATH/'xls_case'/book_name
    book = Databook().load('xls', open(str(book_path), 'rb').read())
    for sheet in book.sheets():
        if sheet.title == sheet_name:
            ret = json.loads(sheet.json)
            return map(parse, ret)
    return []


# 将解析出的case中的float转换成整形
def parse(data):
    temp = {}
    for k, v in data.items():
        if not v:
            continue
        elif isinstance(v, float):
            temp[k] = int(v)
        else:
            temp[k] = v
    return temp


if __name__ == "__main__":
    print('test')
    b_name = 'test'
    s_name = 'test_add'
    # python3解析map时需要加list才能显示
    m = list(gen_xls_data(b_name, s_name))
    print(m)
