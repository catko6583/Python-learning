print("python learning")
print("Loading...")
print("what wil be you'r password?")
password = input()
f = open("password.txt", "w")
f.write(password)
f.close()
print("done")