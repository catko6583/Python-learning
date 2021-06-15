print ("enter your password")
f = open("password.txt", "r")
passwod = input()
if passwod == f.read():
 print("welcome!")
 print ("what you want to learn? enter the number of what you want to learn")
 print ("you can learn now:\n", "if learning number 1")
 iwanttolearn = int(input())
 if iwanttolearn == (1):
     print ("ok wil be today learning if\n","for example:\n", 'if (1+1) == "2":\n', 'print("hi")\n', "it wil print hi or it can be used like this\n", "username = input()\n", 'if username == "catko6583":\n', 'print ("welcome catko6583!")\n', "else:\n", 'print ("wrong username")\n', "if it's catko6583 it wil print welcome catko6583! but if it's something else it wil print wrong username")
     print ("this is only v1 so more things to learn in v2!")
 else:
     print("sorry we could not find that number in the options please try again by rerunning")
else:
    print("wrong try again by rerunning program")