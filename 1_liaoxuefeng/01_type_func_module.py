# -*- coding: utf-8 -*-

def normalize(names):
    def norm_name(name):
        return name[0].upper() + name[1:].lower()
    return list(map(norm_name, names))

def str2float(fstr):
    def char2num(char):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[char]

    def str2num(istr):
        return reduce(lambda x,y: x*10+y, map(char2num, istr))

    if '.' not in fstr:
        fstr += '.0'
    inte = fstr.split('.')[0]
    deci = fstr.split('.')[1]

    return str2num(inte) + str2num(deci) * pow(0.1, len(deci))

def mirror_filter(max):
    def is_mirror(num):
        str = "%d" % num
        return str == str[::-1]
    return filter(is_mirror, range(max))
	
def main():
    printf("I love python!")
    norm_name = normalize(['kite', 'kEVEn', 'HAIPENG'])
    print(norm_name)
    print(str2float("123.1"))

    for num in mirror_filter(100000):
        print(num, end=" ")

if __name__ == '__main__':
    from distutils.log import warn as printf
    from functools import reduce
    main()

