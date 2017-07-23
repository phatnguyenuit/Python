#coding:utf-8
'''
dictionary dạng {key:value, key2:value2,....,key_n:value_n}
truy cập giá trị của dictionary
dictionary['key']
cập nhật giá trị của key bằng cách gán lại giá trị cho dictionary['key']

xoá del ten_dictionary[key]
hoặc del ten_dictionary để xoá tất cả

#dict.clear()
#dict.copy() return a copy
#dict.get(key,default=None)
#dict.items() trả về tất cả cặp key-value
#dict.update(dict2) update dict2 to dict
'''

import calendar
print "Thang hien tai la:"
cal = calendar.month(2014, 6)
print cal