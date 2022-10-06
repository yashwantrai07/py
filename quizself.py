#Using Import
from simple_colors import *
import sys, subprocess
import time
sc=0
chsc=[]
chhc=[]
name=[]
clas=[]
roll=[]
aopt=[]

# Home Screen of The Page
def home ():
    print (green("                      Pop Quiz                                    ",'bold'))
    print("1. Play Quiz")
    print("2. Contact Us")
    print("3. Exit")
    ch=int(input(cyan("Enter your choice (1, 2, 3 or 4)")))
    subprocess.run('clear', shell=True)
    if ch==1 :
        print ("______________________________________")
        playquiz()
        stream()
    if ch==2 :
         print (" Contact Details -")
         print ("Phone -", end = " ")
         print ("9120xxxxxxx")
         print ("Email -", end = " ")
         print ("xyz@gmail.com")
         print ("Address -", end = " ")
         print ("Varanasi, U.P, India")
         print("_____________________________")
         print(yellow("1. Play The Quiz"))
         print(yellow("2. Exit"))
         cho=int(input(cyan("Enter your choice (1 or 2)")))
         if cho==1:
             stream()
         if cho==2:
             print("Bye")
         
    if ch==3 :
         print("Bye")   

               
                              
#Your Details
#Asking you to what do you want to play                                                            
def playquiz() :
    global chsc
    global name
    global clas
    global roll
    file=open("quizdata.txt","a+")
    file1=open("quizdataers.txt","w")
    name=input(yellow("Enter Your Name :",'italic'))
    clas=int(input(yellow("Enter Your Current Class :",'italic')))
    roll=int(input(yellow("Enter Your Roll No :",'italic')))
    subprocess.run('clear', shell=True)
    a=str(roll)
    b=str(clas)
    c=('\n')
    d=('Name :')
    e=('Class :')
    f=('Roll No :')
    end = " "
    end1="_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
    file.write(c)
    file.write(end1)
    file.write(c)
    file.write(c)
    file.write(d)
    file.write(end)
    file.write(name)
    file.write(c)
    file.write(e)
    file.write(end)
    file.write(b)
    file.write(c)
    file.write(f)
    file.write(end)
    file.write(a)
    file.write(c)
    file.close()
  #__________________  
    file1.write(c)
    file1.write(end1)
    file1.write(c)
    file1.write(c)
    file1.write(d)
    file1.write(end)
    file1.write(name)
    file1.write(c)
    file1.write(e)
    file1.write(end)
    file1.write(b)
    file1.write(c)
    file1.write(f)
    file1.write(end)
    file1.write(a)
    file1.write(c)
    file.close()
    
    
def stream():
    global chsc
    global sc
    print("________________________________")
    print(magenta("1. Computer Fundamentals",'bright'))
    print(magenta("2. General Knowledge",'bright'))
    print(magenta("3. Basic Science",'bright'))
    print(magenta("4. Intermediate Python",'bright'))
    chsc = int(input(cyan("Choose the quiz you want to play(1, 2 ,3 or 4)")))
    subprocess.run('clear', shell=True)
    if chsc==1 :        
        computer1()
        computer2()
        computer3()
        computer4()
        computer5()
        computer6()
        computer7()
        computer8()
        computer9()
        computer10()
        scoreee()
        percent()
        append()
        nextlevel()
    if chsc==2:
        sc = 0
        gkquiz1()
        gkquiz2()
        gkquiz3()
        gkquiz4()
        gkquiz5()
        gkquiz6()
        gkquiz7()
        gkquiz8()
        gkquiz9()
        gkquiz10()
        scoreee()
        percent()
        append()
        nextlevel()
    if chsc==3:
        sc=0
        science1()
        science2()
        science3()
        science4()
        science5()
        science6()
        science7()
        science8()
        science9()
        science10()
        scoreee()
        percent()
        append()
        nextlevel()
    if chsc==5:
        sc=0
        python1()
        python2()
        python3()
        python4()
        python5()
        python6()
        python7()
        python8()
        python9()
        python10()
        scoreeee()
        percent()
        append()
        nextlevel()
        
                            
def computer1():    
    global sc
    print("_________________________")
    z = "Q-1 The brain of any computer system is ?"
    p = "A. ALU"
    q = "B. Memory"
    r = "C. CPU"
    s = "D. Desktop"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
        
    if cz == "C":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer2():
    global sc
    print ("_____________________________")
    z = "Q-2 Which of the following is the smallest unit of data in a computer ?"
    p = "A. Bit"
    q = "B. Bytes"
    r = "C. TeraBytes"
    s = "D. KiloBytes"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is",sc)
    else :
          print("Your Current Score is :",sc)    
          
def computer3():
    print ("_____________________________")
    
    global sc
    z = "Q-3 URL stands for ?"
    p = "A. Uniform Resource Research"
    q = "B. Uniform Resource Link"
    r = "C. Uniform Research Locator"
    s = "D. Uniform Resource Locator"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer4():
    global sc
    print ("_____________________________")
    z = "Q-4 Which part interprets program instructions and initiate control operations ?"
    p = "A. Input"
    q = "B. CPU"
    r = "C. Control Unit"
    s = "D. None of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def computer5():
    print ("_____________________________")
    
    global sc
    z = "Q-5 The binary system uses powers of ?"
    p = "A. 1"
    q = "B. 10"
    r = "C. 6"
    s = "D. 2"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer6():
    global sc
    print ("_____________________________")
    z = "Q-6 A computer program that converts assembly language to machine language is ?"
    p = "A. Compiler"
    q = "B. Assembler"
    r =  "C. Interpreter"
    s = "D.  Both A and C"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
                    
def computer7():
    print ("_____________________________")
    
    global sc
    z = "Q-7 The examination and changing of single bits or small groups of his within a word is called ?"
    p = "A. Bit Manipulation"
    q = "B. Bit"
    r = "C.  Bit Slice"
    s = "D. All of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
        
    if cz == "A":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer8():
    global sc
    print ("_____________________________")
    z = "Q-8 ASCII stands for ?"
    p = "A. All purpose scientific code for information interchange"
    q = "B. American standard code for information interchange"
    r = "C. American security code for information interchange"
    s = "D. None of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                             
                                        
def computer9():
    print ("_____________________________")
    
    global sc
    z = "Q-9 Any device that performs signal conversion is ?"
    p = "A. Modem"
    q = "B. Router"
    r = "C. Antenna"
    s = "D. Modulator"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer10():
    global sc
    print ("_____________________________")
    z = "Q-10 Codes consisting of light and dark marks which may be optically read is known as ?"
    p = "A. Decoder"
    q = "B. Mnemonics"
    r = "C. Bar Code"
    s = "D. None of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                                                      
#nextlevel #nextlevel nextlevwl nextlevel nextlevel nextlevel nextlevel nextlevel nextlevel nextlevel nextlevel nextlevwl nextlevel nextlevel nextlevel         

def computer11():
    global sc
    z = "Q-1 The first mechanical calculating machine was made by ?"
    p = "A. Guido van Rossum"
    q = "B. Charles Babbage"
    r = "C. Blaise Pascal"
    s = "D. Bjarne Stroustrup"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
        
    if cz == "C":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)


def computer12():
    global sc
    print ("_____________________________")
    z = "Q-2 Which of the following can be output by a computer ?"
    p = "A. Graphics"
    q = "B. Voice"
    r = "C. Text"
    s = "D. All of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
    if cz == "D":
          sc = sc+1
          print("Your Current Score is",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def computer13():
    print ("_____________________________")
    
    global sc
    z = "Q-3 Which input device is able to scan & interpret an entire page that is typed in a special font ?"
    p = "A. Optical card readers"
    q = "B. Floppy Disk"
    r = "C. Paper tape punch"
    s = "D. Page Reader"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer14():
    global sc
    print ("_____________________________")
    z = "Q-4 A half byte is know is ?"
    p = "A. Nibble"
    q = "B. Bit"
    r = "C. Half Byte"
    s = "D. Byte"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def computer15():
    print ("_____________________________")
    
    global sc
    z = "Q-5 A medium for transferring data between two locations is called ?"
    p = "A. Internet"
    q = "B. Bus"
    r = "C. Modem"
    s = "D. Communication Channel"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer16():
    global sc
    print ("_____________________________")
    z = "Q-6 Primary storage is _____ as compared to secondary storage ?"
    p = "A. Fast and inexpensive"
    q = "B. Fast and expensive"
    r = "C. Slow and inexpensive"
    s = "D. None of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
                    
def computer17():
    print ("_____________________________")
    
    global sc
    z = "Q-7 A sizeable geographical area with communication based on the telephone system is though as ?"
    p = "A. Wide area network"
    q = "B. Local area network"
    r = "C.  Landline"
    s = "D. All of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
        
    if cz == "A":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer18():
    global sc
    print ("_____________________________")
    z = "Q-8 Which of the following is used for manufacturing chips ?"
    p = "A. Control unit"
    q = "B. Bus"
    r = "C. Semiconductor"
    s = "D. None of the above"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                             
                                        
def computer19():
    print ("_____________________________")
    
    global sc
    z = "Q-9 Which of the following terms is the most closely related to main memory ?"
    p = "A. Non-volatile"
    q = "B. Permaneny"
    r = "C. Temporary"
    s = "D. Control unit"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
        
    if cz == "C":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def computer20():
    global sc
    print ("_____________________________")
    z = "Q-10 One nibble is equal to ?"
    p = "A. 2 bits"
    q = "B. 4 bits"
    r = "C. 8 bits"
    s = "D. 16 bits"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                          
#gkquiz gkquiz gkquiz gkquiz gkquiz gkquiz gkquiz gkquiz gkquiz gkquiz gkq                                                                                                                                                        
def gkquiz1():
    print("_________________________")
    global sc
    z = "Q-1 What is the official slogan of the 2024 Paris Olympics ?"
    p = "A. Inclusive and Impressive"
    q = "B. Global Partnership"
    r = "C. Games Wide Open"
    s = "D. Botherly and beautiful"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
        
    if cz == "C":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)


def gkquiz2():
    global sc
    print ("_____________________________")
    z = "Q-2 Who is the richest woman in Asia ?"
    p = "A. Kiran Mazumdar Shah"
    q = "B. Falguni Nayar"
    r = "C. Savitri Jindal"
    s = "D. Radha Vembu"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def gkquiz3():
    print ("_____________________________")
    
    global sc
    z = "Q-3 Which state government has partnered with LinkedIn to boost employability skills of its students ?"
    p = "A. Mumbai"
    q = "B. Hyderabad"
    r = "C. Banglore"
    s = "D. Kerala"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz4():
    global sc
    print ("_____________________________")
    z = "Q-4 India is set to implement joint research projects with which country through Technology Innovation Hubs (TIH) ?"
    p = "A. Russia"
    q = "B. Israel"
    r = "C. USA"
    s = "D. Saudi Arabia"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def gkquiz5():
    print ("_____________________________")
    
    global sc
    z = "Q-5 World Organ Donation Day is celebrated on which date ?"
    p = "A. August 13"
    q = "B. September 1"
    r = "C. September 2"
    s = "D. August 16"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
        
    if cz == "A":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz6():
    global sc
    print ("_____________________________")
    z = "Q-6 Which major central bank announced that it would harmonise how banks offer crypto assets ?"
    p = "A. European Central Bank"
    q = "B. Reserve Bank of India"
    r = "C. Reserve Bank of Australia"
    s = "D. U.S Federal Reserve"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
                    
def gkquiz7():
    print ("_____________________________")
    
    global sc
    z = "Q-7 When is the ‘World Senior Citizen’s Day’ celebrated ?"
    p = "A. September 2"
    q = "B. January 15"
    r = "C.  August 21"
    s = "D.  February 22"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
        
    if cz == "C":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz8():
    global sc
    print ("_____________________________")
    z = "Q-8 Which space agency has spotted Carbon-di-oxide in the atmosphere of an exo-planet ?"
    p = "A. Space X"
    q = "B. NASA"
    r = "C. ISRO"
    s = "D. Rocosmos"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                             
                                        
def gkquiz9():
    print ("_____________________________")
    
    global sc
    z = "Q-9 Who is the first Indian sportsperson to clinch the prestigious Diamond League Meet title ?"
    p = "A. Sachin Tendulkar"
    q = "B. Mahendra Singh Dhoni"
    r =  "C. P.V Sindhu"
    s = "D. Neeraj Chopra"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz10():
    global sc
    print ("_____________________________")
    z = "Q-10 In 2022 India became the country with the highest number of sponsored study visas in which country ?"
    p = "A. USA"
    q = "B. UK"
    r = "C. Russia"
    s = "D. Australia"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                    
                                                                                
#quiz next level next level next level next level next level next level next level mwxt 
def gkquiz11():    
    global sc
    z = "Q-1 Which company has partnered with technology giants such as Meta, Google, Microsoft and Intel to roll out 5G services ?"
    p = "A. Reliance"
    q = "B. Vi"
    r = "C. Bharti Airtel"
    s = "D. Bsnl"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
        
    if cz == "A":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)


def gkquiz12():
    global sc
    print ("_____________________________")
    z = "Q-2 Which country has broken its own record for the world’s lowest fertility rate ?"
    p = "A. China"
    q = "B. Japan"
    r = "C. South Korea"
    s = "D. India"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def gkquiz13():
    print ("_____________________________")
    
    global sc
    z = "Q-3 ‘Rashtriya Poshan Maah’ is observe every year during which month ?"
    p = "A. October"
    q = "B. January"
    r = "C. August"
    s = "D. September"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' D'))
        
    if cz == "D":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz14():
    global sc
    print ("_____________________________")
    z = "Q-4 The ‘International Day for People of African Descent’ was first observed in which year ?"
    p = "A. 2021"
    q = "B. 1947"
    r = "C. 2016"
    s = "D. 2009"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
          
def gkquiz15():
    print ("_____________________________")
    
    global sc
    z = "Q-5 Which Indian state launched the “country’s first virtual school” ?"
    p = "A. New Delhi"
    q = "B. Banglore"
    r = "C. Mumbai"
    s = "D. Uttar Pradesh"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
        
    if cz == "A":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz16():
    global sc
    print ("_____________________________")
    z = "Q-6 As per the RBIs liberalised norms, what is the new limit of External Commercial Borrowing (ECB) under automatic route ?"
    p = "A. USD 1 billion"
    q = "B. USD 1.5 billion"
    r = "C. USD 500 million"
    s = "D. USD 1.6 billion"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
                    
def gkquiz17():
    print ("_____________________________")
    
    global sc
    z = "Q-7 Which Indian state is included in the ‘World’s 50 Greatest Places of 2022’ by Time Magazine ?"
    p = "A. Uttar Pradesh"
    q = "B. Kerala"
    r = "C.  Banglore"
    s = "D.  Bihar"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
        
    if cz == "B":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz18():
    global sc
    print ("_____________________________")
    z = "Q-8 When is the ‘Nelson Mandela Day’ observed every year?"
    p = "A. September 5"
    q = "B. July 18"
    r = "C. April 1"
    s = "D. December 31"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                             
                                        
def gkquiz19():
    print ("_____________________________")
    
    global sc
    z = "Q-9 What is the Goods and Service Tax (GST) for fresh milk and pasteurised milk ?"
    p = "A. 0%"
    q = "B. 5%"
    r =  "C. 2%"
    s = "D. 8%"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D): "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"' A'))
        
    if cz == "A":
         sc = sc+1
         print("Your Current Score is :",sc)
    else :
        print("Your Current Score is :",sc)

def gkquiz20():
    global sc
    print ("_____________________________")
    z = "Q-10 Which country’s super computer has become the fastest in the world ?"
    p = "A. USA"
    q = "B. UK"
    r = "C. Japan"
    s = "D. Australia"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)                                                                                    

                                                                            #science quiz      
                                                                            
def science1() :
    global sc
    print ("_____________________________")
    z = "Q-1 Choose correct example of a herbivore animal ?"
    p = "A. Fox"
    q = "B. Dog"
    r = "C. Goat"
    s = "D. Bear"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc) 
    
    
def science2():
    global sc
    print ("_____________________________")
    z = "Q-2 Which of the following is outermost layer of the earth's atmosphere ?"
    p = "A. Troposphere"
    q = "B. Statosphere"
    r = "C. Exosphere"
    s = "D. Mesosphere"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
def science3():
    global sc
    print ("_____________________________")
    z = "Q-3 Choose the correct example of non-renewable resource ?"
    p = "A. Forest"
    q = "B. Water"
    r = "C. Sunlight"
    s = "D. Soil"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)            
def science4():
    global sc
    print ("_____________________________")
    z = "Q-4 Who Invented Thermometer ?"
    p = "A. Gabrial Daniel Fahrenheit"
    q = "B. Miachel Farady"
    r = "C. Narendra Modi"
    s = "D. Rahul Gandhi"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)

def science5():
    global sc
    print ("_____________________________")
    z = "Q-5 The First Antibiotic' Penicillin' was discovered by ?"
    p = "A. Hakan Calhongalu"
    q = "B. Alexander Fleming"
    r = "C. Louis Suarez"
    s = "D. Kylian Mbappe"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)    
          
def science6():
    global sc
    print ("_____________________________")
    z = "Q-6 How much time does light takes to reach from sun to earth ?"
    p = "A. 1 Minute"
    q = "B. 1 Second"
    r = "C. 7 Minutes 19 Seconds"
    s = "D. 8 Minutes 19 Seconds"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'D'))
    if cz == "D":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)       
          
                                      
def science7():
    global sc
    print ("_____________________________")
    z = "Q-7 Who was the Indian man to go in space?"
    p = "A. Rakesh Sharma"
    q = "B. Yuri Gargarin"
    r = "C. Kalpana Chawla"
    s = "D. Vinicious Junior"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)          
          
          
def science8( ):
    global sc
    print ("_____________________________")
    z = "Q-8 Which of these is a communicable disease ?"
    p = "A. Scurvy"
    q = "B. Cancer"
    r = "C. Anaemia"
    s = "D. Cholera"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'D'))
    if cz == "D":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)


def science9():
    global sc
    print ("_____________________________")
    z = "Q-9 The largest part of the brain is ?"
    p = "A. Cerebellum"
    q = "B. Medulla"
    r = "C. Cerebrum"
    s = "D. Parietal lobe"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)       
          
def science10():
    global sc
    print ("_____________________________")
    z = "Q-10 Asthma and allergies are caused by ?"
    p = "A. Noise Pollution"
    q = "B. Air Pollution"
    r = "C. Water Pollution"
    s = "D. Land Pollution"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)   
          
#next level science quiz
#next level
#next level 
#next level.
def science11() :
    global sc
    print ("_____________________________")
    z = "Q-11 Choose correct example of a herbivore animal ?"
    p = "A. Fox"
    q = "B. Dog"
    r = "C. Goat"
    s = "D. Bear"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc) 
    
    
def science12():
    global sc
    print ("_____________________________")
    z = "Q-12 Which of the following is outermost layer of the earth's atmosphere ?"
    p = "A. Troposphere"
    q = "B. Statosphere"
    r = "C. Exosphere"
    s = "D. Mesosphere"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
def science13():
    global sc
    print ("_____________________________")
    z = "Q-13 Choose the correct example of non-renewable resource ?"
    p = "A. Forest"
    q = "B. Water"
    r = "C. Sunlight"
    s = "D. Soil"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)            
def science14():
    global sc
    print ("_____________________________")
    z = "Q-14 Who Invented Thermometer ?"
    p = "A. Gabrial Daniel Fahrenheit"
    q = "B. Miachel Farady"
    r = "C. Narendra Modi"
    s = "D. Rahul Gandhi"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)

def science15():
    global sc
    print ("_____________________________")
    z = "Q-15 The First Antibiotic' Penicillin' was discovered by ?"
    p = "A. Hakan Calhongalu"
    q = "B. Alexander Fleming"
    r = "C. Louis Suarez"
    s = "D. Kylian Mbappe"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "C":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'C'))
    if cz == "C":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)    
          
def science16():
    global sc
    print ("_____________________________")
    z = "Q-16 How much time does light takes to reach from sun to earth ?"
    p = "A. 1 Minute"
    q = "B. 1 Second"
    r = "C. 7 Minutes 19 Seconds"
    s = "D. 8 Minutes 19 Seconds"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'D'))
    if cz == "D":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)       
          
                                      
def science17():
    global sc
    print ("_____________________________")
    z = "Q-17 Who was the Indian man to go in space?"
    p = "A. Rakesh Sharma"
    q = "B. Yuri Gargarin"
    r = "C. Kalpana Chawla"
    s = "D. Vinicious Junior"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "D":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'D'))
    if cz == "D":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)          
          
          
def science18( ):
    global sc
    print ("_____________________________")
    z = "Q-18 Which of these is a communicable disease ?"
    p = "A. Scurvy"
    q = "B. Cancer"
    r = "C. Anaemia"
    s = "D. Cholera"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)


def science19():
    global sc
    print ("_____________________________")
    z = "Q-19 The largest part of the brain is ?"
    p = "A. Cerebellum"
    q = "B. Medulla"
    r = "C. Cerebrum"
    s = "D. Parietal lobe"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "A":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'A'))
    if cz == "A":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)       
          
def science20():
    global sc
    print ("_____________________________")
    z = "Q-20 Asthma and allergies are caused by ?"
    p = "A. Noise Pollution"
    q = "B. Air Pollution"
    r = "C. Water Pollution"
    s = "D. Land Pollution"
  
    print (z)
    print(p)
    print (q)
    print (r)
    print (s)
    cz = input(cyan("Enter (A, B, C, or D):  "))
    cz = cz.upper()
    if cz == "B":
        print (green("Correct ✓"))
    else :
        print (red("Incorrect, The Right Answer is :"'B'))
    if cz == "B":
          sc = sc+1
          print("Your Current Score is :",sc)
    else :
          print("Your Current Score is :",sc)
          
          
#play again and #play again #play again 
#play again # play again 
# play again #play again #playagain
#play again #playagain  #playagain   #playagain     #playagain

def play():
    global sc
    global chsc
    global chhc
    sc=0
    if chsc==1:
        computer1()
        computer2()
        computer3()
        computer4()
        computer5()
        computer6()
        computer7()
        computer8()
        computer9()
        computer10()
        scoreee()
        percent()
        append()
        nextlevel()    
    if chsc==2:
        gkquiz1()
        gkquiz2()
        gkquiz3()          
        gkquiz4()
        gkquiz5()
        gkquiz6()
        gkquiz7()
        gkquiz8()
        gkquiz9()
        gkquiz10()
        scoreee()
        percent()
        append()
        nextlevel()
    if chsc==3:
        science1()
        science2()
        science3()
        science4()
        science5()
        science6()
        science7()
        science8()
        science9()
        science10()
        scoreee()
        percent()
        append()
        nextlevel()
    if chsc==4:
        python1()
        python2()
        python3()
        python4()
        python5()
        python6()
        python7()
        python8()
        python9()
        python10()
        scoreee()
        percent()
        append()
        nextlevel()


#asking for play again, next level or print personal details or back to home screen

def nextlevel():
    global chhc
    global sc
    print("________________________________")
    print(yellow("1. Play Again"))
    print(yellow("2. Play the next level"))
    print(yellow("3. Play Another Quiz"))
    print(yellow("4. Inspect the Record"))
    print(yellow("5. Show my score details"))
    chhc=int(input(cyan("Enter Your Choice(1, 2, 3, 4 or 5)")))
    if chhc==1:
        play()             
    if chhc == 2:
        again()
    if  chhc ==3:
         stream()
    if chhc ==4:
        getpass()
        nextlevel()
    if chhc ==5:
        mydet()
        nextlevel()
  #playagain play again #playagain playagain play again play again play again play again play again play again
  
                      
def again():
      global sc
      global aopt              
      if sc >= 7:
        print("________________________")
        aopt= input(magenta("You are eligible for next level. Enter (Yes) to play next level"))
        aopt=aopt.upper()
        if aopt== "YES":
            print("____________________________")
            print('\n')
            print(green("                   Welcome to level 2                   ",'bright'))
            sc=0
            play2()
        else:
            
            print("Thanks for Playing")   
            home()
      else:
          print("___________________________")
          print(red("Sorry, You are not eligible for Next level. Minimum Score Required is 7: "))
          print("1. Return to Home Page")
          print("2. Play Again")
          b=int(input("Enter Your Choice (1 or 2)"))
          if b ==1 :
              home()
          if b==2  :
              play()    

 #percent #percent #percent #percent #percent #percent #percent #perencet              
def percent ():
    global sc
    
    per=(sc/10)*100
    print ("Your Percentage is :",per)
    
#total score #total score #total score #total score    
def scoreee():
    global sc
    print("_______________________________")
    print("Your Total Score is",sc)   
    
sc=0

def getpass():
    print("_________________________________")
    print(red("- Only authorised person can access the details."))
    print('\n')
    print(green("                         Login Page                                  ", 'bright'))
    cli2=input(magenta("Enter Username: "))
    cli = input(magenta("Password: "))
    if cli2=="yrai07":
        if cli=="ssps":
            read()
        else:
            print("Wrong Password")
            home()
    else:
        print("Wrong Username")
        home()    
    
    
def append2():
    global aopt
    global sc
    global chsc
    file=open("quizdata.txt","a+")
    file1=open("quizdataers.txt","a+")
    a=("Score of Computer Fundamentals (Level - 2) :")
    b=("Score of General Knowledge (Level -2 ):")
    cz=("Score of Basic Science (Level - 2):")
    d=("Score of Python Quiz (Level - 2):")
    end= " "
    end1='\n'
    z=str(sc)
    if chsc==1:
        if aopt=="YES":
            file.write(a)
            file.write(end)
            file.write(z)
            file.write(end1)
            file1.write(a)
            file1.write(end)
            file1.write(z)
            file1.write(end1)
    if chsc==2:
            if aopt=="YES":
                file.write(b)
                file.write(end)
                file.write(z)
                file.write(end1)
                file1.write(b)
                file1.write(end)
                file1.write(z)
                file1.write(end1)
    if chsc==3:
            if aopt=="YES":
                file.write(cz)
                file.write(end)
                file.write(z)
                file.write(end1)
                file1.write(cz)
                file1.write(end)
                file1.write(z)
                file1.write(end1)
    if chsc==4:
            if aopt=="YES":
                file.write(d)
                file.write(end)
                file.write(z)
                file.write(end1)
                file1.write(d)
                file1.write(end)
                file1.write(z)
                file1.write(end1)
    file.close()
    file1.close
def append():
    global aopt
    global sc
    global chsc
    file=open("quizdata.txt","a+")
    file1=open("quizdataers.txt","a+")
    a=("Score of Computer Fundamentals :")
    b=("Score of General Knowledge :")
    cz=("Score of Basic Science :")
    d=("Score of Python Quiz :")
    end= " "
    end1='\n'
    z=str(sc)
    if chsc==1:
        file.write(a)
        file.write(end)
        file.write(z)
        file.write(end1)
        file1.write(a)
        file1.write(end)
        file1.write(z)
        file1.write(end1)
    if chsc==2:
        file.write(b)
        file.write(end)
        file.write(z)
        file.write(end1)
        file1.write(b)
        file1.write(end)
        file1.write(z)
        file1.write(end1)
    if chsc==3:
        file.write(cz)
        file.write(end)
        file.write(z)
        file.write(end1)
        file1.write(cz)
        file1.write(end)
        file1.write(z)
        file1.write(end1)
    if chsc==4:
        file.write(d)
        file.write(end)
        file.write(z)
        file.write(end1)
        file1.write(d)
        file1.write(end)
        file1.write(z)
        file1.write(end1)
    file.close()
    file1.close()    

        
def mydet():
    a=open("quizdataers.txt","r")
    b=a.read()
    print(b)
    
def read():
    file=open("quizdata.txt","r")
    b=file.read()
    print(b)
    
def nextlevel2():
    global chhc
    global sc
    print("________________________________")
    print(yellow("1. Play Again"))
    print(yellow("2. Play the next level"))
    print(yellow("3. Play Another Quiz"))
    print(yellow("4. Inspect the Record"))
    print(yellow("5. Show my score details"))
    chhc=int(input(cyan("Enter Your Choice(1, 2, 3, 4 or 5)")))
    if chhc==1:
        play()             
    if chhc == 2:
        print("Congratulations, you have reached the maximum level. Please enter any other choice from below")
        nextlevel2()
    if  chhc ==3:
         stream()
    if chhc ==4:
        getpass(prompt)
        nextlevel()
    if chhc ==5:
        mydet()
        nextlevel2() 
        
def nextlevel3():
    global chhc
    global sc
    print("________________________________")
    print(yellow("1. Play Again"))
    print(yellow("2. Play the next level"))
    print(yellow("3. Play Another Quiz"))
    print(yellow("4. Inspect the Record"))
    print(yellow("5. Show my score details"))
    chhc=int(input(cyan("Enter Your Choice(1, 2, 3, 4 or 5)")))
    if chhc==1:
        print("_________________________")
        play2()             
    if chhc == 2:
        print('\n')
        print(green("Congratulations, you have reached the maximum level. Please enter any other choice from below"))
        nextlevel3()
    if  chhc ==3:
         stream()
    if chhc ==4:
        getpass()
        nextlevel()
    if chhc ==5:
        mydet()
        nextlevel2()  
        
        
        
def play2():
    global sc
    global chsc
    global chhc
    sc=0
    if chsc==1:
        computer11()
        computer12()
        computer13()
        computer14()
        computer15()
        computer16()
        computer17()
        computer18()
        computer19()
        computer20()
        scoreee()
        percent()
        append2()
        nextlevel3()    
    if chsc==2:
        gkquiz11()
        gkquiz12()
        gkquiz13()          
        gkquiz14()
        gkquiz15()
        gkquiz16()
        gkquiz17()
        gkquiz18()
        gkquiz19()
        gkquiz20()
        scoreee()
        percent()
        append2()
        nextlevel3()
    if chsc==3:
        science11()
        science12()
        science13()
        science14()
        science15()
        science16()
        science17()
        science18()
        science19()
        science20()
        scoreee()
        percent()
        append2()
        nextlevel3()
    if chsc==4:
        python11()
        python12()
        python13()
        python14()
        python15()
        python16()
        python17()
        python18()
        python19()
        python20()
        scoreee()
        percent()
        append2()
        nextlevel3()
      
#_________________________________________
home()

