# coding=utf-8
import random
import re

def demo_string():
    stra = "hello world"
    print stra.capitalize() # 首字母大写
    print stra.replace("world","nowcoder")
    strb = "  \n\rhello nowcoder \r\n"
    print 1,strb.lstrip()
    print 2,strb.rstrip()
    strc = "hello w"
    print strc.startswith("hel")
    print strc.endswith("w")
    print stra + strb + strc
    print len(strc)
    print '-'.join(['a','b','cc'])
    print strc.split(" ")
    print strc.find("he")


def demo_operation():
    print 3 + 3,3 * 5,4 * 6,16/3
    print True
    print not False
    print 2 << 3,4 >> 2
    x = 2
    print type(x)

def demo_buildinfunction():
    print len([1,2,3])
    print max(2,3,4),min(3,4,5)
    print abs(-3)
    print range(1,10,3)
    print dir(list)
    print chr(97),ord('a')
    print divmod(11,2)

def demo_controller():
    score = 65
    if score > 90:
        print "A"
    elif score > 60:
        print "B"
    else:
        print "C"

    while score < 100:
        print score
        score += 10
    print "----------------"
    for i in range(0,10,2):
        print i
        break

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def demo_list():
    lista = [1,2,3,4,5] # 类似于vector，list
    print lista
    listb = [1,'2',3,1.1]
    print listb
    lista.extend(listb)
    print lista
    print 'a' in lista
    listb.insert(0,'a')
    print listb
    listb.pop(1)
    print listb
    listb.sort()
    print listb
    listb.sort(reverse=True)
    print listb
    listb.append('x')
    print listb

def demo_dict():
    dicta = {'1':2,'2':3,'3':4}
    print dicta
    print dicta.keys(),dicta.values()
    print 3 in dicta
    print dicta.get('4',0)
    for key,value in dicta.items():
        print key,value
    dictb = {"+":add,"-":sub}
    print dictb['+'](1,2)

def demo_set():
    seta = set([1,2,3])
    print seta
    setb = set([2,3,4])
    print seta & setb
    print len(seta)

def demo_except():
    try:
        x = 1 / 0
    except Exception as e:
        print "error:",e
    finally:
        print "clean up"

def demo_random():
    # random.seed(100)
    print random.random()
    print random.randint(0,200)
    print random.choice(range(1,100))
    a = [1,2,3,4,5,6]
    random.shuffle(a)
    print a

def demo_re():
    s = "a123dfh5g~eww3  eeee5"
    res = re.findall("[\d]+?",s)
    b = "daoshangxl@163.com"
    print res
    print re.findall("[163 | qq]+.com",b)

if __name__ == '__main__':
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controller()
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_except()
    # demo_random()
    demo_re()