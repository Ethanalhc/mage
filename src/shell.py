import mage

mage = mage.Mage()

running = True
while running:
    _ = input(">> ")

    try:
        with open(_, "r") as f:
            code = f.read()
    except:
        code = _
    
    mage.run(code)
