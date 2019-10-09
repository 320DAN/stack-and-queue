# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:10:35 2019

@author: Lenovo
"""

#使用数组实现栈
class ArrayStack:
    def __init__(self):
        self.guizi=[]
    def push(self,x):
        self.guizi.append(x)
    def pop(self):
        a=self.guizi.pop()
        return a
tony=ArrayStack()
tony.push('a1')
tony.push('a2')
print(tony.pop())
print(tony.pop())


#使用链表实现栈
class Node:  #创建节点
    def __init__(self,x):
        self.data=x
        self.next=None  #创建两个属性 data next是属性名
    def setData(self,x):
        self.data=x
    def getData(self):
        return self.data
    def setNext(self,n):
        self.next=n
    def getNext(self):
        return self.next
class LinkedStack:
    def __init__(self):
        self.top=None #栈顶指针 当前是空的
    def push(self,x):  #创建节点
        n=Node(x)  #连接节点
        if self.top==None: #为空 不为空
            self.top=n
        else:
            n.setNext(self.top)
            self.top=n
    def pop(self):
        #程序不健壮 会崩溃 所以要有判断
        if self.top==None:
            return None
        else:
            result=self.top.getData()
            self.top=self.top.getNext()
            return result
tony=LinkedStack()
tony.push('u1')
tony.push('u2')
print(tony.pop())
print(tony.pop())
        

#使用数组实现队列
class Queue:
    def __init__(self):
        self.guizi=[]
    def enqueue(self,x):
        self.guizi.append(x)
    def dequeue(self):
        b=self.guizi.pop(0)
        return b
pepper=Queue()
pepper.enqueue('v1')
pepper.enqueue('v2')
print(pepper.dequeue())
print(pepper.dequeue())


#使用链表实现队列
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.items)
    q.dequeue()
    q.dequeue()
    print(q.items)



#实现一个“拉火车”的扑克牌游戏，自动执行的游戏
class Poker:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.suit+self.rank
    def isSame(self, poker):
        return self.rank == poker.rank
class Queue:
    def __init__(self):
        self.data = []
    def enqueue(self, x):
        self.data.append(x)
    def dequeue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)

class Stack:
    def __init__(self):
        self.data = []
    def push(self,x):
        self.data.append(x)
    def pop(self):
        return self.data.pop()
    def size(self):
        return len(self.data)
    def existsSame(self, x):
        for i in self.data:
            if i.isSame(x):
                return True
        return False
    def show(self):
        for x in self.data:
            print(x,end=' ')
        print()

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = Queue()
    def outCard(self):
        return self.hands.dequeue()
    def inCard(self,x):
        self.hands.enqueue(x)
    def countHands(self):
        return self.hands.size()
    def showHands(self):
        return ','.join([str(c) for c in self.hands.data])
import random

class TrainGame():
    def __init__(self, players, num_deck): 
        self.players = [ Player(player) for player in players]
        self.NUM_PLAYERS = len(self.players)
        self.desk = Stack()
        self.__init_deck(num_deck)
    def __init_deck(self, num_deck):
        suits = ['♠','♥','♣','♦']
        ranks = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
        cards = [ Poker(s,r) for s in suits for r in ranks]
        jokers = [Poker('R','M'),Poker('B','M')] # 大王小王
        cards.extend(jokers)
        self.cards = cards* num_deck
    
    def shuffle_cards(self): # 洗牌
        temp = []
        n = len(self.cards)
        for i in range(n):
            temp.append( self.cards.pop( random.randint(0,len(self.cards)-1)))
        for i in range(n):
            self.cards.append( temp.pop(random.randint(0,len(temp)-1)))
    
    def divide_cards(self): # 发牌
        n = len(self.cards)
        for i in range(n):
            self.players[i%self.NUM_PLAYERS].inCard(self.cards.pop(0))
    
    def play(self):
        alive = self.players.copy()
        i = 0 # 总出牌次数
        idx_who_next = 0 # 要出牌人的索引 
        while True:
            # 如果人数少于2人，则结束
            if len(alive)<2:
                print("GAME OVER")
                break
            # who_next出牌 1 取出一张牌，2 判断是否可以收牌， 3 判断是否出局
            who = alive[idx_who_next]
            card = who.outCard()
            if card:
                # 如果桌牌存在，则收牌，
                if self.desk.existsSame(card):
                    who.inCard(card)
                    while True:
                        c = self.desk.pop()
                        who.inCard(c)
                        if c.isSame(card):
                            break
                else: # 否则，牌到桌上
                    self.desk.push(card)
            if who.countHands()==0:
                alive.remove(who)
            # 计算下一个出牌人索引
            idx_who_next += 1
            idx_who_next %= len(alive)
            print("=============================== ROUND #{} {} {} ==========".format(i,who.name,str(card) if card else "NONE"))
            self.show()
            i+=1
    
    def show(self):
        print(" =========== players ===========")
        for p in self.players:
            print(p.name, p.showHands())
        print(" ========== desk ==============")
        self.desk.show()
        
a = TrainGame(['lilei','hanmm'],1)
a.shuffle_cards()
a.divide_cards()
a.play()















