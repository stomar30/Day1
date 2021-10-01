class Library:
    def __init__(self,bookList,):
        self.bookList = bookList

    def display(self):
        for book in self.bookList:
            print(book)
        

    def issue(self):
        bName = input("Enter the book name u want to issue: ")
        if bName in self.bookList:
            self.bookList.remove(bName)
            print("Book has issued to you")
        else:
            print("Book is not present in booklist or already issued")

        
        

    def submit(self,sub):
        self.bookList.append(sub)
        print("Book has been submitted")

bookList = ["maths","physics","chemistry", "biology","english","science"]

s = Library(bookList)


while(True):
    choice = int(input("pls choose any one option:\n1.Display\n2.Isuue\n3.Submit\n "))

    if choice == 1:
        s.display()
    elif choice == 2:
        s.issue()
    elif choice == 3:
        sub = ("Enter the book u want to submit:")
        s.submit(sub)
        
    else:
        print("Invalid input")

    choice2 = input("Press q to quite and c to continue: ")
    if choice2 == "q":
        exit()
    elif choice2 == "c":
        continue




    