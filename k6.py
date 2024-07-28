import matplotlib.pyplot as plt
class kc_mat_plot(object):
    def __init__(self):
        self.col=[]
    def drawline(self):
        plt.plot(self.col)
        plt.show()
    def additem(self,data):
        if data not in self.col:
            self.col.append(data)
            print('item added in collection....')
        else:print('pls enter item....')
    def drawline4(self,title,xtitle,ytitle,color):
        plt.plot(self.col,marker='*',mec='red',mfc='yellow',ms='43',linewidth='23')
        plt.title(title)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.show()
if __name__=='__main__':
    ob=kc_mat_plot()
    ob.additem(4)
    ob.additem(6)
    ob.additem(2)
    ob.drawline4('abacus','point','yellow','orange')
    print('---------------')
    ob.additem(8)
    ob.additem(5)
    ob.additem(3)
    ob.drawline4('abacus','point','pink','orange')
