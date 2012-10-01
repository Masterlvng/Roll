# -*- coding:utf-8 -*-
from random import randint
class Roll():


    def __init__(self):
        
        self.NameList = []

    def shuffle(self,start,end,nums):
        try:
            length = end -start + 1
            assert (end - start)>=0 and  nums >0 and nums <=length
            List = [i for i in range(start,end+1)]
            for j in range(nums):
                ch=randint(start,end)
                yield List[ch-1]
                List.remove(List[ch-1])
                end = end -1
        except AssertionError:
            print 'Argument illegal!'


    def Rock(self):
        print '''Welcome to lottery System. 
        By Masterlvng@McDoing'''
        print '''Input Your choice
        1:抽数字
        2:抽人名(从文件中读取人名)'''
        while True:
            option = int(raw_input('>>>'))
            if option not in [1,2]:
                print '输入有误,重新输入'
            else:
                break
        if option ==1:
            args = raw_input('输入取值范围.格式如 "1-3"\n')
            nums = int(raw_input('抽奖名额数.\n'))
            arg_list=args.split('-')
            try:
                assert arg_list[0].isdigit() and arg_list[1].isdigit()
                print '输入"next"得到下一个获奖序号,输入其他,将停止抽奖\n'
                for seq in self.shuffle(int(arg_list[0]),int(arg_list[1]),nums):
                    cmd = raw_input('>>>')
                    if cmd == 'next':
                        print seq
                    else:
                        break

            except AssertionError,ValueError:
                print 'Argument illegal!'
        else:
            filename = raw_input('输入文件名:')
            try:
                with open(filename,'r') as f:
                    self.NameList = f.readlines()
                Length = len(self.NameList)
                print '成功读取名单'
                raw_counts=raw_input('要抽取多少个?\n')
                counts = int(raw_counts)
                assert raw_counts.isdigit() and 1<=counts and counts<=Length
                print '输入"next"得到下一个获奖姓名,输入其他,将停止抽奖\n'
                for seq in self.shuffle(0,Length-1,counts):
                    cmd=raw_input('>>>')
                    if cmd == 'next':
                        print '恭喜',self.NameList[seq]
                    else:
                        break




            except IOError:
                print filename,'不存在'
            except AssertionError:
                print '参数错误'
        print '抽奖结束'


                    



            


        
