'''os is built in moudle in python which allows many functions
to do with directoriees and files'''
import os
# this chdir() command changes current working directory#
os.chdir('C:\\Users\Muhammad Jawad\Desktop\Python_practice')
# getcwd command elist current working directory#
x=os.getcwd()
print(x)
# listdor() command enlist all directories#
x=os.listdir()
print(x)
# mkdir command create new directory
os.mkdir('test')
# rename command changes name of directory rename(old_name,new_name#)
os.rename('test','Python_OOP')