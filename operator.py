#coding:utf-8
'''
    #Toán tử số học
    //	Thực hiện phép chia, trong đó kết quả là thương số sau khi đã xóa các chữ số sau dấu phảy
    +	Phép cộng
    -	Phép trừ
    *	Phép nhân
    /	Phép chia
    %	Phép chia lấy phần dư
    **	Phép lấy số mũ (ví dụ 2**3 cho kết quả là 8)

    #Toán tử quan hệ
    <	Nhỏ hơn. Nếu giá trị của toán hạng trái là nhỏ hơn giá trị của toán hạng phải, thì điều kiện trở thành true
    >	Lớn hơn
    <=	Nhỏ hơn hoặc bằng
    <=	Lớn hơn hoặc bằng
    ==	Bằng
    !=	Không bằng
    <>	Không bằng (tương tự !=)

    #Toán tử logic
    and	Phép Và. Nếu cả hai điều kiện là true thì kết quả sẽ là true
    or	Phép Hoặc. Nếu một trong hai điều kiện là true thì kết quả là true
    not	Phép phủ định. Được sử dụng để đảo ngược trạng thái logic của toán hạng

    #Toán tử bit
    a = 0011 1100 và b = 0000 1101.

    &	AND Sao chép một bit tới kết quả nếu bit này tồn tại trong cả hai toán hạng	(a & b) cho kết quả 0000 1100
    |	OR Sao chép một bit tới kết quả nếu bit này tồn tại trong bất kỳ toán hạng nào	(a | b) = 61 (tức là 0011 1101)
    ^	XOR Sao chép bit nếu nó được set (chỉ bit 1) chỉ trong một toán hạng	(a ^ b) = 49 (tức là 0011 0001)
    ~	NOT Đây là toán tử một ngôi, được sử dụng để đảo ngược bit	(~a ) = -61 (tức là 1100 0011)
    <<	Toán tử dịch trái nhị phân. Giá trị của toán hạng trái được dịch chuyển sang trái một số lượng bit đã được xác định bởi toán hạng phải	a << 2 = 240 (tức là 1111 0000)
    >>	Toán tử dịch phải nhị phân. Giá trị của toán hạng trái được dịch chuyển sang phải một số lượng bit đã được xác định bởi toán hạng phải	a >> 2 = 15 (tức là 0000 1111)
    
    #Toán tử membership
    in	Trả về true nếu một biến là nằm trong dãy các biến, nếu không là false
    not in	Trả về true nếu một biến là không nằm trong dãy các biến, nếu không là false

    #Toán tử identify
    is	Trả về true nếu các biến ở hai bên toán tử cùng trỏ tới một đối tượng, nếu không là false
    is not	Trả về false nếu các biến ở hai bên toán tử cùng trỏ tới một đối tượng, nếu không là true

    #NOTE
    import thư viện division để phép chia ra số thực
    from __future__ import division
'''
print "Operator!"
