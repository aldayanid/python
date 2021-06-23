def is_compliant(psswrd:str)->bool:
    return len(psswrd)>=8 and any(chr.isdigit() for chr in psswrd)
    
def main():
    psswrd=input("Password: ")
    if is_compliant(psswrd):
        print("OK")
    else:
        print("Wrong")
  
if __name__ == '__main__':
    main()