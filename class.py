class myclass():
    def __init__(self,m) :
        self.model=m
    def show(self,p):
        price=p
        print("model is ", self.model ,"and price is ",p)
obj1=myclass("iphone ")
print(obj1.model)
obj1.show(110000)


       
