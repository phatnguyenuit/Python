#coding:utf-8
'''
Việc lập chỉ mục của cả hai hướng đều được cung cấp bởi sử dụng String trong Python:

-Chỉ mục với hướng forward bắt đầu với 0,1,2,3,…
-Chỉ mục với hướng backward bắt đầu với -1,-2,-3,…

'''
var1 = 'Hello World!\a'
var2 = "Python Programming"
name = "Phat Nguyen"

print var1
print 2 * var1
print var1 * 2
print var1[0]
print var1[:4]
print var1[1:4]
print var1[:-2]
print var1[-2:]

print 'Toi ten la %s nang %d kg' %(name,70)

'''
Phương thức capitalize()
	-Viết hoa chữ cái đầu tiên của chuỗi
Phương thức center(width, fillchar)
	-Trả về một chuỗi mới, trong đó chuỗi ban đầu đã được cho vào trung tâm và hai bên đó là các fillchar sao cho tổng số ký tự của chuỗi mới là width
Phương thức count(str, beg= 0,end=len(string))
	-Đếm xem chuỗi str này xuất hiện bao nhiêu lần trong chuỗi string hoặc chuỗi con của string nếu bạn cung cấp chỉ mục ban đầu start và chỉ mục kết thúc end
Phương thức decode(encoding='UTF-8',errors='strict')
	-Giải mã chuỗi bởi sử dụng encoding đã cho
Phương thức encode(encoding='UTF-8',errors='strict')
	-Trả về phiên bản chuỗi đã được mã hóa của chuỗi ban đầu. 
    -Nếu có lỗi xảy ra, thì chương trình sẽ tạo một ValueError trừ khi các lỗi này được cung cấp với ignore hoặc replace
Phương thức endswith(suffix, beg=0, end=len(string))
	-Xác định xem nếu chuỗi string hoặc chuỗi con đã cho của string (nếu bạn cung cấp chỉ mục bắt đầu beg và chỉ mục kết thúc end) kết thúc với hậu tố suffix thì trả về true, nếu không thì phương thức này trả về false
Phương thức expandtabs(tabsize=8)
	-Mở rộng các tab trong chuỗi tới số khoảng trống đã cho; mặc định là 8 space cho mỗi tab nếu bạn không cung cấp tabsize
Phương thức find(str, beg=0 end=len(string))
	-Xác định xem chuỗi str có xuất hiện trong chuỗi string hoặc chuỗi con đã cho của string (nếu bạn cung cấp chỉ mục bắt đầu beg và chỉ mục kết thúc end), nếu xuất hiện thì trả về chỉ mục của str, còn không thì trả về -1
Phương thức index(str, beg=0, end=len(string))
	-Tương tự như find(), nhưng tạo ra một ngoại lệ nếu str là không được tìm thấy

Phương thức isalnum()
	-Trả về true nếu chuỗi có ít nhất một ký tự và tất cả ký tự là chữ-số. Nếu không hàm sẽ trả về false

Phương thức isalpha()
	-Trả về true nếu chuỗi có ít nhất 1 ký tự và tất cả ký tự là chữ cái. Nếu không phương thức sẽ trả về false

Phương thức isdigit()
	-Trả về true nếu chuỗi chỉ chứa các chữ số, nếu không là false
Phương thức islower()
	-Trả về true nếu tất cả ký tự trong chuỗi là ở dạng chữ thường, nếu không là false
Phương thức isnumeric()
	-Trả về true nếu một chuỗi dạng Unicode chỉ chứa các ký tự số, nếu không là false
Phương thức isspace()
	-Trả về true nếu chuỗi chỉ chứa các ký tự khoảng trắng whitespace, nếu không là false
Phương thức istitle()
	-Trả về true nếu chuỗi là ở dạng titlecase, nếu không là false
Phương thức isupper()
	-Trả về true nếu tất cả ký tự trong chuỗi là chữ hoa
Phương thức join(seq)
	-Nối chuỗi các biểu diễn chuỗi của các phần tử trong dãy seq thành một chuỗi
Phương thức len(string)
	-Trả về độ dài của chuỗi
Phương thức ljust(width[, fillchar])
	-Trả về một chuỗi mới, trong đó có chuỗi ban đầu được căn chỉnh vào bên trái và bên phải là các fillchar sao cho tổng số ký tự là width
Phương thức lower()
	-Chuyển đối tất cả chữ hoa trong chuỗi sang kiểu chữ thường
Phương thức lstrip()
	-Xóa tất cả các khoảng trống trắng ban đầu (leading) trong chuỗi
Phương thức maketrans()
	-Trả về một bảng thông dịch được sử dụng trong hàm translate
Phương thức max(str)
	-Trả về ký tự chữ cái lớn nhất từ chuỗi str đã cho
Phương thức min(str)
	-Trả về ký tự chữ cái nhỏ nhất từ chuỗi str đã cho
Phương thức replace(old, new [, max])
	-Thay thế tất cả sự xuất hiện của old trong chuỗi với new với số lần xuất hiện max (nếu cung cấp)
Phương thức rfind(str, beg=0,end=len(string))
	-Tương tự hàm find(), nhưng trả về chỉ mục cuối cùng
Phương thức rindex( str, beg=0, end=len(string))
	-Giống index(), nhưng trả về chỉ mục cuối cùng nếu tìm thấy
Phương thức rjust(width,[, fillchar])
	-Trả về một chuỗi mới, trong đó có chuỗi ban đầu được căn chỉnh vào bên phải và bên trái là các fillchar sao cho tổng số ký tự là width
Phương thức rstrip()
	-Xóa bỏ tất cả các khoảng trống trắng ở cuối (trailing) của chuỗi
Phương thức split(str="", num=string.count(str))
	-Chia chuỗi theo delimeter đã cho (là space nếu không được cung cấp) và trả về danh sách các chuỗi con; nếu bạn cung cấp num thì chia chuỗi thành num chuỗi con
Phương thức splitlines( num=string.count('\n'))
	-Trả về một List gồm tất cả các dòng trong chuỗi, và tùy ý xác định các ngắt dòng (nếu num được cung cấp và là true).
Phương thức startswith(str, beg=0,end=len(string))
	-Xác định xem chuỗi hoặc chuỗi con (nếu bạn cung cấp chỉ mục bắt đầu beg và chỉ mục kết thúc end) có bắt đầu với chuỗi con str không, nếu có trả về true, nếu không là false
Phương thức strip([chars])
	-Thực hiện cả hai phương thức lstrip() và rstrip() trên chuỗi
Phương thức swapcase()
	-Đảo ngược kiểu của tất cả ký tự trong chuỗi
Phương thức title()
	-Trả về một bản sao của chuỗi trong đó tất cả ký tự đầu tiên của tất cả các từ là ở kiểu chữ hoa.
Phương thức translate(table, deletechars="")
	-Trả về một bản sao đã được thông dịch của chuỗi
Phương thức upper()
	-Chuyển đổi các chữ thường trong chuỗi thành chữ hoa
Phương thức zfill (width)
	-Trả về một chuỗi mới, trong đó bao gồm chuỗi ban đầu và được đệm thêm với các số 0 vào bên trái sao cho tổng ký tự là width
Phương thức isdecimal()
	-Trả về true nếu một chuỗi dạng Unicode chỉ chứa các ký tự thập phân, nếu không là false
'''