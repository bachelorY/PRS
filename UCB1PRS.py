import random
import math
import tkinter
import time

'''
定义石头为 2
剪刀为 1
布为 0
'''
historyGame=[] # 历史对局 里面是一个个字典,用来存放对局信息,包括,各个参赛者的猜拳,和局数
ROCK = 2
SCISSORS = 1
PAPER = 0


# def judge(max,min):
#         if max == 0 and min == 2 :
#             return 1
#         elif max == 2 and min == 0:
#             return -1
#         else: 
#             return max - min

class Judge():
    def __init__(self):
        self.competitorWin=[0] * 2
        self.num = 0
        

    def tkInit(self):
        # 图形化界面需要用到的变量
        self.count = 0
        self.competitor1Wincount = 0
        self.competitor2Wincount = 0

        # 图形化界面
        self.root = tkinter.Tk()
        self.root.title("石头剪刀布大战") 
        self.root.minsize(1000,450)
        
        self.notification = tkinter.StringVar() # 用来显示消息的对话框
        self.notification.set('欢迎!开始石头剪刀布的比拼吧!')
        self.layout()
        self.root.mainloop()

    def layout(self):        
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), textvariable=self.notification)
        show_label.place(x=100, y=20, width=800, height=70)

        HvsC_btn = tkinter.Button(self.root,text="人机对战",command=self.HvsC)
        HvsC_btn.place(x=100, y=120, width=800, height=70)
        CvsC_btn = tkinter.Button(self.root,text="机器对战",command=self.CvsC)
        CvsC_btn.place(x=100, y=220, width=800, height=70)
        
    def HvsC(self):
        self.root.destroy()
        humam = Human()

    def CvsC(self):
        self.root.destroy()
        self.CvsCroot = tkinter.Tk()
        self.CvsCroot.title("机器对战")
        self.CvsCroot.minsize(1000,450)
        self.CvsCnotification = tkinter.StringVar()
        self.CvsCnotification.set("生成参赛选手中")
        show_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 30), textvariable=self.CvsCnotification)
        show_label.place(x=100, y=20, width=800, height=70)
        self.selectAndStart()
        # self.CvsCroot.after(500,self.showDetails)
        self.showDetails()
        self.CvsCroot.mainloop()

        

        
    def showDetails(self):
        if self.count >= self.num :
            return 
        self.count+=1
        notice = "下面开始第" + str(self.count) + "轮比赛"
        self.CvsCnotification.set(notice)
        show_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 30), textvariable=self.CvsCnotification)
        show_label.place(x=100, y=20, width=800, height=70)
        # 显示选手们的出手
        competitor1_text = tkinter.StringVar()
        competitor1_text.set("一号参赛选手出的是:")
        competitor1_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 14), textvariable=competitor1_text)
        competitor1_label.place(x=100, y=120, width=200, height=70)
        self.showChoice(self.count-1,'competitor1')
        competitor2_text = tkinter.StringVar()
        competitor2_text.set("二号参赛选手出的是:")
        competitor2_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 14), textvariable=competitor2_text)
        competitor2_label.place(x=500, y=120, width=200, height=70)
        self.showChoice(self.count-1,'competitor2')
        # 显示选手们的获胜次数
        self.showWin()
        # self.showChoice(count-1)
        self.CvsCroot.after(500,self.showDetails)  
            
    def showWin(self):
        result = historyGame[self.count-1]['result']
        if result == 1:
            self.competitor1Wincount +=1
            resultText = "一号  胜"
        elif result == -1:
            self.competitor2Wincount += 1
            resultText = "二号  胜"
        else:
            resultText = "平    局"

        result_text = tkinter.StringVar()
        result_text.set(resultText)
        result_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 14), textvariable=result_text)
        result_label.place(x=380,y=270)
        win_text = tkinter.StringVar()
        win_text.set("获胜次数:")
        win_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 14), textvariable=win_text)
        win_label.place(x=20,y=320)
        competitor1Win_text = tkinter.StringVar()
        competitor1Win_text.set(self.competitor1Wincount)
        competitor1Win_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 14), textvariable=competitor1Win_text)
        competitor1Win_label.place(x=150,y=370)
        competitor2Win_text = tkinter.StringVar()
        competitor2Win_text.set(self.competitor2Wincount)
        competitor2Win_label = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 14), textvariable=competitor2Win_text)
        competitor2Win_label.place(x=550,y=370)
        

    def selectAndStart(self):
        competitorList = []
        mabPlayer = MABPlayer()
        competitorList.append(mabPlayer)
        copyplayer = CopyPlayer()
        competitorList.append(copyplayer)
        randomplayer = RandomPlayer()
        competitorList.append(randomplayer)
        simpleplayer = SimplePlayer()
        competitorList.append(simpleplayer)
        competitor1 = random.choice(competitorList)
        competitor2 = random.choice(competitorList)
        while competitor1 == competitor2 or competitor1 == copyplayer:
            competitor1 = random.choice(competitorList)
        self.start(100,competitor1,competitor2)
    
    def showChoice(self,num,competitor):
        # global RGif,SGif,PGif # tkinter.PhotoImage不能显示图片却不报错的问题
        # RGif = tkinter.PhotoImage(file='R.gif')
        # SGif = tkinter.PhotoImage(file='S.gif')
        # PGif = tkinter.PhotoImage(file='P.gif')
        # choice = historyGame[num][competitor]
        # if choice == 2: # 选择展示的图片
        #     choiceimag=RGif
        # elif choice == 1:
        #     choiceimag=SGif
        # else:
        #     choiceimag=PGif
        # if competitor == 'competitor1':
        #     choice_label = tkinter.Label(self.CvsCroot,imag=choiceimag)
        #     choice_label.place(x=350,y=220)
        # else:
        #     choice_label = tkinter.Label(self.CvsCroot,imag=choiceimag)
        #     choice_label.place(x=550,y=220)
        # 无法实现两个label同时展示图片,放弃图片显示
        choice = historyGame[num][competitor]
        choice_text = tkinter.StringVar()
        if choice == 2: # 获取选手的选择
            choice_text.set("石头")
        elif choice == 1:
            choice_text.set("剪刀")
        else:
            choice_text.set("布  ")
        if competitor == 'competitor1':
            choice_label1 = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 24), textvariable=choice_text)
            choice_label1.place(x=150,y=220)
        else:
            choice_label2 = tkinter.Label(self.CvsCroot, bd=3, bg='white', font=('宋体', 24), textvariable=choice_text)
            choice_label2.place(x=550,y=220)

    # def showChoice(self,num):
    #     global RGif,SGif,PGif # tkinter.PhotoImage不能显示图片却不报错的问题
    #     RGif = tkinter.PhotoImage(file='R.gif')
    #     SGif = tkinter.PhotoImage(file='S.gif')
    #     PGif = tkinter.PhotoImage(file='P.gif')
    #     canvas = tkinter.Canvas(self.CvsCroot,width=500,height=100)
        

    #     choice = historyGame[num]['competitor1'] # 一号选手
    #     if choice == 2: # 选择展示的图片
    #         choice1imag=RGif
    #     elif choice == 1:
    #         choice1imag=SGif
    #     else:
    #         choice1imag=PGif
    #     canvas.create_image(100, 100, anchor='w', image=choice1imag)

    #     choice = historyGame[num]['competitor2'] # 二号选手
    #     if choice == 2: # 选择展示的图片
    #         choice2imag=RGif
    #     elif choice == 1:
    #         choice2imag=SGif
    #     else:
    #         choice2imag=PGif
    #     canvas.create_image(100, 100, anchor='e', image=choice2imag)
        
    #     canvas.pack()

    def judge(self,competitor1,competitor2):
        if competitor1 == 0 and competitor2 == 2 :
            return 1
        elif competitor1 == 2 and competitor2 == 0:
            return -1
        else: 
            return competitor1 - competitor2
    
    def start(self,num,competitor1,competitor2):
        self.num = num
        while(num>0):
            c1Select = competitor1.select()
            c2Select = competitor2.select()
            result = self.judge(c1Select,c2Select)
            if result == 1:
                self.competitorWin[0] += 1
            elif result == -1:
                self.competitorWin[1] += 1
            # historyGame.append({'num':self.num-num,'competitor1':c1Select,'competitor2':c2Select,'result':result})
            historyGame.append({'competitor1':c1Select,'competitor2':c2Select,'result':result})
            num -= 1
    
    def showRate(self):
        print('competitor1: %.2f\ncompetitor2: %.2f' %(self.competitorWin[0] / self.num, self.competitorWin[1] / self.num))

    def showHistory(self):
        for i in range(self.num):
            print(historyGame[i])

    def newgame(self):
        self.competitorWin=[0] * 2
        self.num = 0
        historyGame=[]



class MABPlayer(): # 将利用MAB决策的玩家看作拉杆个数为3的多臂老虎机,其中每个拉杆的回报概率分别是出石头,剪刀,布获胜的概率;
    def __init__(self):
        # self.win = [0,0,0,0,0,0]# 前三项用来存储各个手势的胜率,后三个用来存储各个手势的出手次数
        self.win = [0] * 3 # 用来存储各个手势的胜率
        self.visits = [0,0,0] # 用来记录出各个手势的次数
        self.step=0
        self.choose=None # 记录最后一次出手,方便更新

    def randomSelect(self): # 一开始我们让玩家随机出手
        self.choose = random.randint(0,2)
        self.visits[self.choose] += 1
        self.step += 1
        return self.choose
    
    def update(self):
            if historyGame == []:
                pass
            else:
                result = historyGame[self.step-1]['result']
                # if result == 1:
                #     win = self.choose
                #     self.win[win+3] += 1
                #     visits = self.win[3] + self.win[4] + self.win[5]
                #     self.win[PAPER] = self.win[PAPER+3] / visits
                #     self.win[SCISSORS] = self.win[SCISSORS+3] / visits
                #     self.win[ROCK] = self.win[ROCK+3] / visits
                     
                # elif result == -1:
                #     win = (self.choose - 1 + 3) % 3
                #     self.win[win+3] += 1
                #     visits = self.win[3] + self.win[4] + self.win[5]
                #     self.win[PAPER] = self.win[PAPER+3] / visits
                #     self.win[SCISSORS] = self.win[SCISSORS+3] / visits
                #     self.win[ROCK] = self.win[ROCK+3] / visits
                # else:
                #     win = (self.choose - 1 + 3) % 3
                #     self.win[win+3] += 0.5
                #     win = (self.choose + 1 + 3) % 3
                #     self.win[win+3] += 0.5
                #     visits = self.win[3] + self.win[4] + self.win[5]

                #     self.win[PAPER] = self.win[PAPER+3] / visits
                #     self.win[SCISSORS] = self.win[SCISSORS+3] / visits
                #     self.win[ROCK] = self.win[ROCK+3] / visits
                
                if result == 1:
                    self.win[self.choose] += 1

    def UCB1Select(self):
        bestucb1 = -1
        bestchoose = None
        
        for choose in range(0,3):
            if self.visits[choose] == 0:
                self.choose = choose
                self.visits[self.choose] += 1
                self.step += 1
                return self.choose
            else:
                # ucb1 = self.win[choose] + math.sqrt(2 * math.log(self.step) / self.visits[choose])
                ucb1 = (self.win[choose] / self.visits[choose]) + math.sqrt(2 * math.log(self.step) / self.visits[choose])
                if bestucb1 < ucb1:
                    bestucb1 = ucb1
                    bestchoose = choose
        self.choose = bestchoose
        self.visits[self.choose] += 1
        self.step += 1    
        
        return self.choose


    def select(self):
        self.update()
        if self.choose == None:
            return self.randomSelect()
        else:
            self.choose = self.UCB1Select()
            return self.choose

class SimplePlayer(): # 采用赢留输变策略的玩家,用于测试多臂老虎机模型
    def __init__(self):
        self.choose=None
        self.step=0
    def randomSelect(self):
        self.choose = random.randint(0,2)
        self.step += 1
        return self.choose
    def select(self):
        if self.choose == None:
            return self.randomSelect()
        else:
            result = historyGame[self.step-1]['result']
            if result == -1: # 赢留输变对策
                self.step += 1
            elif result == 0:
                self.choose = self.randomSelect()
            else: # 输了变成克制上一把的手势
                self.choose = (self.choose - 1 + 3) % 3
                self.step += 1
        return self.choose
    
class CopyPlayer(): # 只会复制对手上局出什么的玩家
    def __init__(self):
        self.choose=None
        self.step=0
    def randomSelect(self):
        self.choose = random.randint(0,2)
        self.step += 1
        return self.choose
    def select(self):
        if self.choose == None:
            return self.randomSelect()
        else:
            self.choose = historyGame[self.step-1]['competitor1']            
        return self.choose

class RandomPlayer(): 
    def __init__(self):
        self.choose=None
        self.step=0
    def randomSelect(self):
        self.choose = random.randint(0,2)
        self.step += 1
        return self.choose
    def select(self):          
        return self.randomSelect()

class Human():
    def __init__(self):
        self.judge = Judge()
        self.mabPlayer = MABPlayer()
        self.tkInit()

    def tkInit(self):
        # 图形化界面
        self.root = tkinter.Tk()
        self.root.title("石头剪刀布大战") 
        self.root.minsize(1000,450)
        
        self.notification = tkinter.StringVar() # 用来显示消息的对话框
        self.notification.set('欢迎!开始石头剪刀布的比拼吧!')
        self.layout()
        self.root.mainloop()

    def layout(self):        
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), textvariable=self.notification)
        show_label.place(x=100, y=20, width=800, height=70)
        
        global RGif,SGif,PGif # tkinter.PhotoImage不能显示图片却不报错的问题
        RGif = tkinter.PhotoImage(file='D:/Program1/python/ai/R.gif')
        SGif = tkinter.PhotoImage(file='D:/Program1/python/ai/S.gif')
        PGif = tkinter.PhotoImage(file='D:/Program1/python/ai/P.gif')
        RButton = tkinter.Button(self.root, image=RGif,command=self.chooseR)
        RButton.place(x=100,y=325)
        SButton = tkinter.Button(self.root, image=SGif,command=self.chooseS)
        SButton.place(x=400,y=325)        
        PButton = tkinter.Button(self.root, image=PGif,command=self.chooseP)
        PButton.place(x=700,y=325)
        # 将choose函数分开写是为了解决command不能传参的问题,网上使用匿名函数只能解决第一次传参问题,之后还是有问题
        
    def select(self):
        return self.choose

    def show_competitor(self):
        competitor = historyGame[len(historyGame)-1]['competitor1']
        choose = historyGame[len(historyGame)-1]['competitor2']
        RSPlist = ["布","剪刀","石头"]
        notice = "你的对手出的是"+RSPlist[competitor]+"你出的是"+RSPlist[choose]
        self.notice = tkinter.StringVar()
        self.notice.set(notice)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), textvariable=self.notice)
        show_label.place(x=100, y=120, width=800, height=70)
        
    def show_result(self):
        result = historyGame[len(historyGame)-1]['result']
        if result == -1:
            self.notice = tkinter.StringVar()
            self.notice.set("恭喜!你获胜了,开始下一次猜拳吧!")
            show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), textvariable=self.notice)
            show_label.place(x=100, y=240, width=800, height=70)
        elif result == 1:
            self.notice = tkinter.StringVar()
            self.notice.set("可惜!失败了,再来一次吧!")
            show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), textvariable=self.notice)
            show_label.place(x=100, y=240, width=800, height=70)           
        else:
            self.notice = tkinter.StringVar()
            self.notice.set("哎呀,是平局!下局决胜负!")
            show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), textvariable=self.notice)
            show_label.place(x=100, y=240, width=800, height=70)

    def chooseR(self):
        self.choose = 2
        self.judge.start(1,self.mabPlayer,self)
        self.show_competitor()
        self.show_result()
            

    def chooseS(self):
        self.choose = 1
        self.judge.start(1,self.mabPlayer,self)
        self.show_competitor()
        self.show_result()
            

    def chooseP(self):
        self.choose = 0
        self.judge.start(1,self.mabPlayer,self)
        self.show_competitor()
        self.show_result()
            







def main():
    
    # 生成裁判和比赛选手
    judge = Judge()
    judge.tkInit()
    # mabPlayer = MABPlayer()
    
    # print("打无脑玩家")
    # copyplayer = CopyPlayer()
    # judge.start(1000,mabPlayer,copyplayer)
    # judge.showRate()
    # judge.newgame()

    # print("打随机玩家")
    # randomplayer = RandomPlayer()
    # judge.start(1000,mabPlayer,randomplayer)
    # judge.showRate()
    # judge.newgame()

    # print("打赢留输变玩家")
    # simplePlayer = SimplePlayer()
    # judge.start(1000,mabPlayer,simplePlayer)
    # judge.showRate()
    # judge.newgame()
    # judge.showHistory()
    
    # print("与人类玩家玩")
    # humam = Human()
    # judge.start(1000,mabPlayer,humam)
    # judge.showRate()
    

if __name__ == '__main__':
    main()