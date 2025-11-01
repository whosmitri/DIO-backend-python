
# allows control flow diversion when certain logical expressions are met

### IF ###
# tests the logical expression and, if it returns true, the actions present in the "IF" code block will be executed

print("### EXAMPLES ###")

print("#### ONE ####")
balance = 2000.0
withdraw = float(input("enter the withdrawal amount: "))

if balance >= withdraw:
    print("withdrawal completed")

else:
    print("insufficient funds")

###

print("#### TWO ####")
opcao = int(input("Choose an option: \n[1] Withdraw \n[2] Statement"))

if (opcao == 1):
    valor = float(input("Enter the withdrawal amount: "))
    # ...
elif (opcao == 2):
    print("Displaying statement...")
else:
    print("Invalid option!")

###

print("#### THREE - NESTED IF ####")

normal_account = True
student_account = False

balance = 2000
withdrawal = 500
overdraft_limit = 450

if (normal_account):
    if (balance >= withdrawal):
        print("Withdrawal successful")
    elif(withdrawal <= (balance + overdraft_limit)):
        print("Withdrawal made using overdraft")
    else:
        print("Withdrawal could not be completed, insufficient funds")
elif (student_account):
    if (balance >= withdrawal):
        print("Withdrawal successful!")
    else:
        print("Insufficient funds")
else:
    print("The system did not recognize the account type, please contact your manager")

###

print("#### THREE - TERNARY OPERATOR ####")

# syntax:
#   value_if_true if condition else value_if_false
# 
# value_if_true: this is the value that will be returned if the condition evaluates to True.
# if condition: this is the Boolean expression that is evaluated.
# else value_if_false: this is the value that will be returned if the condition evaluates to False. 

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)