#coding: utf-8
class Sinhvien:
    'Class co so chung cho tat ca sinh vien'
    svCount = 0

    def __init__(self, ten, hocphi):
        self.ten = ten
        self.hocphi = hocphi
        Sinhvien.svCount += 1
    
    def displayCount(self):
        print "Tong so Sinh vien %d" % Sinhvien.svCount

    def displaySinhvien(self):
        print "Ten : ", self.ten,  ", Hoc phi: ", self.hocphi
        
    def test(self,**kwargs):
        for key,value in kwargs.iteritems():
            print key,value

if __name__ == '__main__':
    '''Lenh nay tao doi tuong dau tien cua lop Sinhvien'''
    sv1 = Sinhvien("Hoang", 4000000)
    '''Lenh nay tao doi tuong thu hai cua lop Sinhvien'''
    sv2 = Sinhvien("Huong", 4500000)
    sv1.displaySinhvien()
    sv2.displaySinhvien()
    print "Tong so Sinh vien %d" % Sinhvien.svCount
    print (getattr(sv1,'tuoi',None))

    '''
    Hàm getattr(obj, name[, default]) : Để truy cập thuộc tính của đối tượng.

    Hàm hasattr(obj,name) : Để kiểm tra xem một thuộc tính có tồn tại hay không.

    Hàm setattr(obj,name,value) : Để thiết lập một thuộc tính. Nếu thuộc tính không tồn tại, thì nó sẽ được tạo.

    Hàm delattr(obj, name) : Để xóa một thuộc tính.
    '''
    hasattr(sv1, 'tuoi')    # Tra ve true neu thuoc tinh 'tuoi' ton tai
    getattr(sv1, 'tuoi',None)    # Tra ve gia tri cua thuoc tinh 'tuoi'
    setattr(sv1, 'tuoi', 20) # Thiet lap thuoc tinh 'tuoi' la 20
    delattr(sv1, 'tuoi')    # Xoa thuoc tinh 'tuoi'

    print "Sinhvien.__doc__:", Sinhvien.__doc__
    print "Sinhvien.__name__:", Sinhvien.__name__
    print "Sinhvien.__module__:", Sinhvien.__module__
    print "Sinhvien.__bases__:", Sinhvien.__bases__
    print "Sinhvien.__dict__:", Sinhvien.__dict__


    '''
    def funct(arg1,arg2,*args):
        #do sth
    def funct(arg1,arg2,**kwargs):
        # get option with name like key-value pair
        access by : kwargs.get("name of variable")
        #do sth
    '''
    sv1.test(name="PhatNguyen",age=19)
    sv1.test(name="PhatNguyen",age=19,gender=True)

    