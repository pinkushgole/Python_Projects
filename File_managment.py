import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"!!! File Name {filename} Create succesfull !!!")
    except FileExistsError:
        print(f"{filename} alredy exixt !!!")
    except Exception as e:
        print("An error accoured !!!")


def view_all_file():
    file=os.listdir()
    if file is None:
        print("!!! No File Found !!!")
    else:
        print("All Files :- ")
        for f in file:
            print(f)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"!!! {filename} is removed !!!")
    except FileNotFoundError:
        print(f"{filename} not Found !!!")
    except Exception as e:
        print("An error accoured !!!")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            print(f"The Content '{filename}' File :-\n{content}")
    except FileNotFoundError:
        print(f"{filename} not Found !!!")
    except Exception as e:
        print("An error accoured !!!")

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("Enter data to add : ")
            f.write(content+'\n')
            print(f"Content add in '{filename}' succesfully")
    except FileNotFoundError:
        print(f"{filename} not Found !!!")
    except Exception as e:
        print("An error accoured !!!") 


def main_fun():
        while True:
            print()
            print('!!! FILE MANAGMENT APP !!!')
            print('1 : Create file')
            print('2 : View All files')
            print('3 : Read file')
            print('4 : Edit file')
            print('5 : Delete file')
            print('6 : Exit')

            choice=input("Enter Your Choice : ")

            if choice=='1':
                filename=input("Enter the file name to create : ")
                create_file(filename)
            elif choice=='2':
                view_all_file()
            elif choice=='3':
                filename=input("Enter the file to read : ")
                read_file(filename)
            elif choice=='4':
                filename=input("Enter the file to read : ")
                edit_file(filename)
            elif choice=='5':
                filename=input("Enter the file you want Delete : ")
                delete_file(filename)
            elif choice=='6':
                print("Closing the app.....")
                break
            else:
                print("!!! Enter the Valid Choice !!!")

main_fun()
