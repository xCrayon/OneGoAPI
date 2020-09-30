import json


def get_category(categories):
    _sub_str = ""

    for category in categories:
        id = category['CategoryId']
        code = category['CategoryCode']
        name = category['CategoryName']

        if name == '全部':
            continue

        grade = category['Grade']
        picture_url = category['PictureUrl']
        parent = category['PriorId']

        _sub_str += "('%s', '%s', '%s', %s, '%s', '%s'),\n" % (id, code, name, grade, picture_url, parent)

        if category['Childs']:
            _sub_str += get_category(category['Childs'])

    return _sub_str


with open('category.json', 'rb') as f:
    category_dict = json.load(f)
    all_category = category_dict['Data']['CategoryList']

    sql = 'INSERT INTO tb_category(id,code,name,grade,picture_url,parent) VALUES '

    sub_str = get_category(all_category)

    with open('category.sql', 'w', encoding='utf-8') as sql_f:
        sql_f.write(sql+'\n'+sub_str)

