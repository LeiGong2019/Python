
# 转义字符
print("hello \nworld!")    
#\ + 转义功能的首字母， n，是newline的首字母，表示换行

print('hello\tworld !') 
print('hello000\tworld')
# t，是一组4个空格
# 你会发现，hello   world !的\t,只占用了3个空格；hello000        world的\t，占用了4个空格； 
# 是因为制表位为4个字符，hell是一个制表位，o占用了第二个制表位的一个空格，所以此时的\t是3个空格；

print('hello\rworld')
# \r，r是return的首字母，表示将光标移动到本行的开头；
# world将hello覆盖了；只输出world

print('hello\bworld')
# \b,是backspace首字母，
# 是退一个字符，会将0覆盖掉了；


print('D:\\nfile')
print(r'D:\nfile')
# r，原字符，不希望字符串中的转义字符其作用； 原字符，就是在前面加r或R；