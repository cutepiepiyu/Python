class MyNewClass:
    """This class is Demonstrates the creation of objects."""
    num=100

    def hello(self):
        print("Hello Word")

obj=MyNewClass()

print(obj.num)
obj.hello()
print(MyNewClass.__doc__) 
"""the last print(.__doc__) can print the comment line"""
