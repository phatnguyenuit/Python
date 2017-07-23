#coding: utf-8
#dữ liệu list thay đổi
list1 = ['vatly', 'hoahoc', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4 = list1 + list2

print list1
print list4

list4.remove(4)
print list4

a = list4.pop(2);
print a;
print list4
#len(list) trả về số phần tử của list
#max(list),min(list),cmp(list1,list2)
#list(tuple) chuyển tuple thành  list

#Dùng toán tử * để lặp thêm n phần tử vào list
#dùng hàm list.append(item) để thêm item cuối list
#xoá phần tử bằng del(list[index]) hoặc list.remove(object)
#list.count()
#list.extend(seq) nối seq vào cuối list
#list.index(obj) trả về index của object trong list
#list.insert(obj,index)
#list.pop(index=-1) xoá và trả về item cuối của list(mặc định) hoặc item ở vị trí index
#list.remove(obj)
#list.reverse() đảo list
#list.sort(function[])
