Filepath="todos.txt"
def get(filepath=Filepath):
    with open(filepath, 'r') as file:
        read_local = file.readlines()
        return read_local

def wrt(lis,filepath=Filepath):
    with open(filepath, 'w') as file:
        file.writelines(lis)

if __name__=='main':

    print("hello")