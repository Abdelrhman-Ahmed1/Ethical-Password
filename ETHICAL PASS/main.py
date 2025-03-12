import socket, os, time, sys, re, random

class Menu:
    
    def displayMenu(self):
        
        print(" \033[34m_____  _____  _____  _____  _____  _____  _____  _____________  _____  _____  _____  _____ \n"+
                "|| \033[31mE\033[34m |||| \033[31mT\033[34m |||| \033[31mH\033[34m |||| \033[31mI\033[34m |||| \033[31mC\033[34m |||| \033[31mA\033[34m |||| \033[31mL\033[34m |||| * * * * * |||| \033[31mP\033[34m |||| \033[31mA\033[34m |||| \033[31mS\033[34m |||| \033[31mS\033[34m ||\n"+
                "||___||||___||||___||||___||||___||||___||||___||||___________||||___||||___||||___||||___||\n"+
                "|/___\\||/___\\||/___\\||/___\\||/___\\||/___\\||/___\\||/___________\\||/___\\||/___\\||/___\\||/___\\|\n")
                    
    
    def displayOptions(self):
        
            print(f"\033[32m==================\033[31m[ ETHICAL TOOL FOR PASSWORD CRACKER & STRENGTH CHECKER ]\033[32m==================\033[0m\n")    
            print("\033[32m[OPTIONS] ( use -h to display options )\033[0m")
            print("  [1] PASSWORD CRACKER ( rockyou.txt must be in the same directory )")
            print("  [2] PASSWORD STRENGTH CHECKER")
            print("  [3] PASSWORD GENERATOR")
            print("  [0] EXIT TOOL")
    
    def getCommand(self):
        
        command = input("<EP> ")   
        
        try:
            
            command = int(command)
            
            if command == 2:
                
                password = input("please enter your password: ")
                print("SCANNING YOUR PASSWORD ...")
                check = passChecker(password)
                
                print("\n\033[35mStrength Level: \033[0m", check.startProcess()[0])
                
                check.feedback.append("\n")
                for x in check.feedback:
                    print(f'\033[33m{x}\033[0m')    
                
                del check
                return self.getCommand()
                
                
                
            elif command == 1:
                
                password = input("please enter your password: ")
                
                counter = 0
                result = ""
                startTime = time.time()
                
                with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as file:
                        
                        for line in file:
                            line = line.strip()
                            if len(line) > 30:
                                continue
                            if str(line) == str(password):
                                result = f"\033[33m[{time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime))}] {counter} ATTEMPTS OF CRACKING YOUR PASSWORD -> {line.strip()}\033[0m"
                                result += "\n\033[34mPassword Cracked Successfully, DON'T CHALLENGE ME\033[0m\n"
                                print(result)
                                return self.getCommand()
                            
                            sys.stdout.write(f"\033[33m[{time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime))}] {counter} ATTEMPTS OF CRACKING YOUR PASSWORD -> {line.strip()}\033[0m\n")
                            sys.stdout.write("\033[F\033[K")
                            
                            sys.stdout.flush()
                            line = file.readline()
                            counter += 1
                        else:           
                            result = f"\033[33m[{time.strftime("%H:%M:%S", time.gmtime(time.time() - startTime))}] {counter} ATTEMPTS OF CRACKING YOUR PASSWORD -> {line.strip()}\033[0m"
                            result += "\n\033[31mPassword Not Cracked\033[0m, Your Password is very \033[31mUNIQUE\033[0m\n" 
                            print(result) 
                            return  self.getCommand()
                    
                
            elif command == 3:
                generate = passGenerator()
                generatedPassword = generate.startProcess()
                print(f"\n\033[33mYour generated password is -> \033[32m{generatedPassword}\033[0m\n")  
                del generate
                return self.getCommand()   
                
                
                
                
                
            elif command == 0:
                count = 3
                while count > 0:
                    sys.stdout.write(f"Exiting tool in \033[31m{count}\033[0m seconds...\n")
                    time.sleep(1)
                    sys.stdout.write("\033[F\033[K")
                    sys.stdout.flush()
                    count -= 1
                os.system("cls")
            else:
                    
                print("Error: command not found")
                return self.getCommand()
                            
        except Exception as e: 
            if command == "":
                return self.getCommand() 
            
            if not command:
                return self.getCommand()
            
            if command == "-h":
                    self.displayOptions()
                    return self.getCommand()
            # print(e)           
            print("Error: command not found")
            return self.getCommand()   
                    

class passChecker:
    
    def __init__(self, password, score = 0):
        self.password = password
        self.score = score
        self.feedback = []
         
    def isCommonPassword(self):
        
        commonPass = [ "123456789", "password", "password123", "123456", "pass12345", "12345", "0000"]
        for x in commonPass:
            if self.password in x:
                return True
        return False
    
    def checkCharacters(self):
        
        if re.search(r'[!@#$%^&*(),.?<>{}]', self.password):
            self.score += 1
        else:
            self.feedback.append("-> Add at least one character (!@#$%^&*(),.?<>{}...)") 
        
        if re.search(r'[a-z]', self.password):
            self.score += 1
        else:
            self.feedback.append("-> Use lowercase letters...") 
        
        if re.search(r'[A-Z]', self.password):
            self.score += 1
        else:
            self.feedback.append("-> Use uppercase letters...")
        
        if re.search(r'[0-9]', self.password):
            self.score += 1
        else:
            self.feedback.append("-> Use numbers...")    
        
        if len(self.password) >= 12:
            self.score += 2
        elif len(self.password) >= 8:
            self.score += 1   
        else:
            self.feedback.append("-> Password should be at least 8 characters...")                      

    def getLevel(self):     
        
        if self.score == 0:
            strengthLevel = f"\033[31mVERY WEAK\033[0m"
        if self.score == 1:   
            strengthLevel = f"\033[31mWEAK\033[0m" 
        if self.score == 2:
            strengthLevel = f"\033[33mMODERATE\033[0m"
        if self.score == 3:
            strengthLevel = f"\033[33mSTRONG\033[0m"
        if self.score == 4:
            strengthLevel = f"\033[32mVERY STRONG\033[0m"
        if self.score >= 5:                
            strengthLevel = f"\033[32mEXCELLENT\033[0m"
            
        return strengthLevel, ""
    
    def startProcess(self):
        
        if self.isCommonPassword():
            self.feedback.append("\033[33mIt is a common password\033[0m")
            return "\033[31mVERY WEAK\033[0m", ""
        else:
            self.checkCharacters()
            return self.getLevel()    
    
    def __dir__(self):
        self.feedback = []    


class passGenerator:
    def __init__(self):
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.numbers = "0123456789"
        self.symbols = "!@#$%^&*(),.?<>"
    
    def startProcess(self):
        all_chars = self.lower + self.upper + self.numbers + self.symbols
        password = ''.join(random.sample(all_chars, 12))
        return password   
    
    
        
                                                                                                                                                                
                                                                                                                                                         
m = Menu()
m.displayMenu()
m.displayOptions()
m.getCommand()



