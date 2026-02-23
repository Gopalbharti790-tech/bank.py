balance=0.0
username=""
user=""
pwd=""
kyc_documents={}
print("==================================================================")
print("welcome to ABC bank")
print("==================================================================")

def signup():
        global user,pwd
        name=input("enter your name : ")
        father_name=input("enter your father name : ")
        mother_name= input("enter your mother name : ")
        user=input("create username : ")
        pwd=(input("create password : "))
        signup_document={}
        document =int(input("enter number of document : "))
        for i in range(document):
            key= input("enter the document type: ")
            value= input("enter the document id  : ")
            signup_document[key]=value
            
def login():
    global user,pwd,username
    username=input("enter your user name: ")
    password=input("enter your password: ")
        
    if user == username:
        if pwd == password:
                print("==================================================================")
                print("login successfully")
                print("==================================================================")
        elif pwd != password:
            
                print("==================================================================")
                print("password incorrect")
                print("==================================================================")
    else:
            print("==================================================================")
            print("user doesn't exist")
            print("==================================================================")

def check_balance():
    print("==================================================================")
    print(f"your current balance is : {balance}")
    print("==================================================================")
    
def deposit_money(amount):
    if amount >0:
        global balance
        balance += amount
    else:
        print("==================================================================")
        print(" deposit amount should be positive or more than 0")
        print("==================================================================")
        
def withdraw_money(amount):
    global balance
    if amount<= 0 or amount>balance:
        print("==================================================================")
        print("withdraw amount should be positive or more than zero")
        print("==================================================================")
    else:
        balance-= amount
        print("==================================================================")
        print(f"the {amount} has been withdrawn successfully")
        print("==================================================================")
        
def check_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)
    
def check_documents():
    if len(kyc_documents)==0:
        print("==================================================================")
        print("KYC not updated")
        print("==================================================================")
    else:
        for doc in kyc_documents:
            print(f"{doc:{kyc_documents[doc]}}")
            
if __name__ =="_main_":
    while True:
        print("1. signup")
        print("2. login")
        print("3. check your balance")
        print("4. deposit an amount")
        print("5. withdrawn amount")
        print("6. KYC status")
        print("7. upload KYC document")
        print("8. quit")
        
        print("==================================================================")
        choose= int(input("enter your choice between 1-8 : "))
        print("==================================================================")
    
        if choose==1:
            signup()
            print("==================================================================")
            print("your account has been open")
            print("==================================================================")
            
        elif choose ==2:
            login()
            print("==================================================================")
            print(f"welcome {username}")
            print(f"now choose the tasks that you want to perform between 3-8 : ")
            print("==================================================================")
                    
        if choose == 3:
            check_balance()
            
        elif choose==4:
            amt=float(input(("enter the amount you have to deposit :")))
            deposit_money(amt)
            
        elif choose == 5:
            amt = float(input("enter the withdrawn amount : "))
            withdraw_money(amt)
            
        elif choose == 6:
            check_documents()
        
        elif choose == 7:
            kyc_docs={}
            document =int(input("how many document you want to upload : "))
            for i in range(document):
                key= str(input("enter those document you want to upload : "))
                value= input("enter the document id : ")
                kyc_docs[key]=value
                
                check_kyc(kyc_docs)
                print("==================================================================")
                print("kyc updated")
                print("==================================================================")
            
        elif choose == 8:
            break
        elif choose >8  :
            print("==================================================================")
            print("invalid enter")
            print("==================================================================")
print("thanks to visiting our bank ")