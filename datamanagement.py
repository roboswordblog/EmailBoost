def getUser(username):
    file = open('data/users.txt', 'r')
    for line in file.read().split("\n"):
        a = line.split(',')
        if a[0] == username:
            return a
    return None


def addUser(username, gmail, password):
    file = open('data/users.txt', 'r')
    for line in file.read().split("\n"):
        a = line.split(',')
        if a[0] == username:
            return True
        if a[2] == gmail:
            return True

    file = open('data/users.txt', 'a')
    file.write(f"\n{username},{gmail},{password},free")
    file.close()


def changeUserPassword(username, password, newpassword):
    file = open('data/users.txt', 'r')


def upgradeUser(username, to):
    file = open('data/users.txt', 'r')
    copy = file.read()
    file.close()
    file = open('data/users.txt', 'w')
    for line in copy.split("\n"):
        if line.strip() == "":
            continue
        a = line.split(',')
        if a[0] == username:
            a[3] = to
        file.write(",".join(a) + "\n")
    file.close()

def getTier(username):
    file = open('data/users.txt', 'r')
    for line in file.read().split("\n"):
        a = line.split(',')
        if a[0] == username:
            return a[3]

