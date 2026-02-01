import mage

mage = mage.Mage()

print("--~                                                  ~--")
print("                 Welcome to Mage v0.1.3                 ")
print("                  Mage is in PRE-ALPHA                  ")
print("Error Handling is not set up, expect poor error phrasing")
print("--~                                                  ~--")

while True:
    _ = input(">> ")

    try:
        with open(_, "r") as f:
            code = f.read()
    except:
        code = _
    
    mage.run(code)
