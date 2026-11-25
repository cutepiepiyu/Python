# single level inheritance
class Parent:
    def parent(self):
        print("This is a method from the Parent class.")

class Child(Parent):
    def child(self):
        print("This is a method from the Child class.")

c = Child()
c.parent()  
c.child()  

#multi level inheritance
class Grandparent:
    def grandparent(self):
        print("This is a method from the Grandparent class.")   
class Parent(Grandparent):
    def parent(self):
        print("This is a method from the Parent class.")
class Child(Parent):
    def child(self):
        print("This is a method from the Child class.")

c = Child()
c.grandparent()
c.parent()
c.child()

#multiple inheritance
class Father:
    def father(self):
        print("This is a method from the Father class.") 
class Mother:
    def mother(self):
        print("This is a method from the Mother class.")
class Child(Father, Mother):
    def child(self):
        print("This is a method from the Child class.")

c = Child()
c.father()
c.mother()
c.child()   

#hierarchical inheritance\
class securitysystem:
    def monitor(self):
        print("Network is being monitored.")
class ids(securitysystem):
    def detect(self):
        print("IDS detect suspicious activities.")
class ips(securitysystem):
    def ips(self):
        print("IPS prevent malicious activities.")

i=ids()
p=ips()

i.monitor()
i.detect()
p.monitor() 
p.ips() 