msg1=input('Enter 1st String:')
msg2=input('Enter 2nd string: ')
f= open('example.txt','w',encoding='utf-8')
f.write(msg1+'\n'+msg2)
f.close()
