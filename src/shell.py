import mage

mage = mage.Mage()

while True:
    _ = input(">> ")

    try:
        with open(_, "r") as f:
            code = f.read()
    except:
        code = _
    
    mage.run(code)
