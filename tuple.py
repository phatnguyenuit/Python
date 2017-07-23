#coding:utf-8
#tuple dữ liệu k đổi
myTuple = (1,2,3);
tup = () # tuple rỗng
tup1 = (1,) # phải có dấu , để cho tuple 1 item
#tuple có thể chứa tuple khác
tupA = ('b','c')
tupB = tupA,('d',)
print tupB
print myTuple

#truy cập tương tự list theo kiểu [start:end] mặc định k co start thì start = 0
#toán tử + nối và * nhân => tạo ra tuple mới
