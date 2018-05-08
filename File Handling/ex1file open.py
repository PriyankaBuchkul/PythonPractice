'''with open('square.txt','w') as f:
      for i in range(1,5):
            f.write('The Square of {} is {}\n'.format(i,i*i))
f.close()

with open('square.txt','r') as s:
      for i in s.readlines():
            print(i)
s.close()
'''

s="""Streaming means listening to music or watching video in ‘real time’, instead of downloading a file to your computer
      and watching it later." Streaming is particularly useful when
      a media consumer's Internet connection speed would allow the
      m to download media completely in less time than it would take to
      view"""

with open("data.txt",'w+') as f:
      f.writelines(s)

s=open("data.txt",'r')
#s.read()
      '''
with open("data.txt",'r')as s:
      for i in s.readlines():
            print(i)
            
#lg=''
#for i in s:
 #     if len(i)>len(lg):
  #          lg=i

#print(lg)



print(s.isatty())
print((s.fileno()))

print("tell==",s.tell())
print("seek==",s.seek(0,2))
print("seekable==",s.seekable())
print("flush==",s.flush())
'''
#f.close()

