import two
print("top level in three.py")
two.two()
def three():
    print("yayyyy!!!")
three()
if __name__=="__main__":
    print("three run direcly")
else:
    print("two.py hab been imported")

