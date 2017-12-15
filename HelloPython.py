import sys
import io
# encoding: utf-8
# sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
print("Hello Python!")

if True:
    print ("True")
else:
    print ("False")


#多行语句
#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
total = "item_one" + \
        "item_two" + \
        "item_three"
print(total)

#在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
#数据类型
#python中数有四种类型：整数、长整数、浮点数和复数。
#整数， 如 1
#长整数 是比较大的整数
#浮点数 如 1.23、3E-2
#复数 如 1 + 2j、 1.1 + 2.2j

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

print(word)
#input()
#help(input)
#等待用户输入
#执行下面的程序在按回车键后就会等待用户输入：
#!/usr/bin/python3
#input("enter")
#input("\n\n按下 enter 键后退出。")
#以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下键时，程序将退出。
#同一行显示多条语句
#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
#!/usr/bin/python3

x = 'runoob'; sys.stdout.write(x + '\n')

#尝试VS code 进行github链接
