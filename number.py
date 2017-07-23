#coding:utf-8
''' 
#Khai báo biến không cần kiểu dữ liệu
    Dùng từ khoá 'del' để xoá biến
    vd : del bien1, bien2,....,bien_n
    Để chuyển đổi kiểu số chỉ cần gọi tên kiểu cần đổi như là một hàm

#Nhóm hàm toán học
    Hàm abs(x)  Trị tuyệt đối của x
    Hàm ceil(x) Số nguyên nhỏ nhất mà không nhỏ hơn x
    Hàm cmp(x, y)   Trả về -1 nếu x < y, trả về 0 nếu x == y, hoặc 1 nếu x > y
    Hàm exp(x)  Trả về ex
    Hàm fabs(x) Giá trị tuyệt đối của x
    Hàm floor(x)    Số nguyên lớn nhất mà không lớn hơn x
    Hàm log(x)  Trả về lnx, với x> 0
    Hàm log10(x)    Trả về log10(x), với x> 0 .
    Hàm max(x1, x2,...) Trả về số lớn nhất
    Hàm min(x1, x2,...) Trả về số nhỏ nhất
    Hàm modf(x) Trả về phần nguyên và phần thập phân của x. Cả hai phần có cùng dấu với x và phần nguyên được trả về dưới dạng một số thực
    Hàm pow(x, y)   Trả về giá trị của x**y.
    Hàm round(x [,n])   Làm tròn x về n chữ số sau dấu thập phân. Python làm tròn theo cách sau: round(0.5) là 1.0 và round(-0.5) là -1.0
    Hàm sqrt(x) Trả về căn bậc hai của x, với x > 0
'''
import math
a = 9.19
print math.ceil(a)