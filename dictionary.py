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

dictA = {'name': 'PhatNguyen', 'age' :23, 'gender' : 'male'};
print 'for loop with key and value by dict.iteritems()'
for key, value in dictA.iteritems():
    print key,' : ',value

print 'for loop with key by dict.iterkeys()'
for key in dictA.iterkeys():
    print key,' : ', dictA[key]

print 'for loop with key by dict.itervalues()'
for value in dictA.itervalues():
    print value