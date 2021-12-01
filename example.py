from pickaxeman.core import *

if __name__ == "__main__":
    pam = Pickaxeman()
    
    # To keep compatibility
    pam.cn_only = True

    print(pam.run())
