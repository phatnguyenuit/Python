# coding: utf-8
'''
sys : Module trong Python cung cấp sự truy cập tới bất kỳ tham số dòng lệnh nào thông qua sys.argv. Phục vụ hai mục đích:

sys.argv là danh sách các tham số dòng lệnh.
len(sys.argv) là số tham số dòng lệnh.
'''

import sys
import getopt

args = sys.argv
print 'So tham so :', len(args), 'tham so.'
print 'Danh sach tham so: ', str(args)