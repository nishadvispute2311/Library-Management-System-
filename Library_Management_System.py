from prompt_toolkit import prompt
import getpass
import datetime as dt

def gettime():
	return dt.datetime.now()


class Library:
	def __init__(self,list_of_books):
		self.booklist=list_of_books
		self.book_data=[]
		self.lentdata=[]
		self.returndata=[]
	
	# To display the books present in the library
	def display(self):
		for index,books in enumerate(self.booklist):
			print(f"{index+1}  :  {books}")
	
	# To keep the data of to whom the book is been given
	def lend_book(self , name_of_taker , bookname , bookindex):
		taker_details=f"Name  :  {name_of_taker}    BookName  :  {bookname}"
		self.book_data.append(taker_details)
		with open("lender_details_database.txt","a") as op:
			op.write(f"{str(gettime())}   {taker_details} \n")
			op.close()
		print(f"Book {bookname} is given successfully to {name_of_taker}........!!! \n")
		del self.booklist[bookindex-1]
		#print(self.book_data)
			
	
					
	# To keep the record of the returned books
	def return_book(self , name_of_returner , name_of_book):
		match_bookdata = f"Name  :  {name_of_returner}    BookName  :  {name_of_book}"
		with open("lender_details_database.txt") as f:
			record=f.readlines()
		with open("lender_details_database.txt","w") as op:
			for data in record:
				if ((name_of_returner not in data) and (name_of_book not in data)):
					op.write(data)
			op.close()
			
		if match_bookdata in self.book_data:
			self.book_data.remove(match_bookdata)
			self.booklist.append(name_of_book)
			with open("Return_details_database.txt","a") as rd:
				rd.write(f"{str(gettime())}   {match_bookdata} \n")
				rd.close()
			
			print(f"Book Returned Successfully.......Thank You {name_of_returner}......")
		else:
			print("Sorry......Failed to return the book.......")
				
	# To check the lent data
	def book_lent(self):
		#for index,lenderdetails in enumerate (self.lentdata):
			#print(f"{index+1}  -->>  {lenderdetails}")
		with open("lender_details_database.txt") as ldd:
			record=ldd.readlines()
			for data in record:
				print(data,end="")
	
	#To check the return books data
	def book_return(self):
		with open("Return_details_database.txt") as rdd:
			record=rdd.readlines()
			for data in record:
				print(data,end="")
	
	# To add the books which one donates to the library
	def add_books(self,Newbook):
		self.booklist.append(Newbook)
		print(f"The Book {Newbook} added successfully to the Library.......")
	
	# To delete the books in the library
	def delete_book(self,bookindex):
		print(f"The book {self.booklist[bookindex-1]} deleted successfully from the Library.......")
		del self.booklist[bookindex-1]
	
	def search_book(self , book_to_search):
		book=book_to_search
		result=[]
		for book_name in self.booklist:
			if book in book_name:
				result.append(book_name)
		print(f"{len(result)} Results are found for your search")
		for index,search_found in enumerate(result):
			print(f"{index+1} --> {search_found}")
	
	def register(self):
		print("\nFollow the Registration Process......!!!!")
		name=input("Enter your full name :  ")
		email=input("Enter your official email :  ")
		username=f"{name.split()[0]}@gescoe_lib"
		password=prompt("Create password :  ",is_password=True)
		confirm_password=prompt("Confirm your password :  ",is_password=True)
		print(f"Your library membership username = {username}")
		if (password==confirm_password):
			with open("Username.txt","a") as op:
				op.write(f"{name.split()[0]}  :  {username}       {password}\n")
				op.close()
				print("Registration Successful...!!!!\n")
				self.login()
		else:
			print("The password does not match........!!!")
			self.register()
	
	def delete_member(self , name_of_member):
		with open ("Username.txt","r") as op:
				member_info = op.readlines()
		with open("Username.txt","w") as f:
				for data in member_info:
					if name_of_member.split()[0].lower() != data.split()[0].lower():
							f.write(data)
				print(f"{name_of_member} is deleted successfully......")
				
		
	def login(self):
		u_list=[]
		p_list=[]
		print("\nEnter your login details.....!!!")
		username=input("Enter username :  ")
		password=prompt("Enter password :  ",is_password=True)
		with open("Username.txt" , "r") as u_name:
			for line in u_name:
				line=line.split()
				u_list.append(line[2])
				p_list.append(line[3])
			u_name.close()
			if((username in u_list) and (password in p_list)):
				print("Successfully Login.....!!!")
				main()
			else:
				print("Incorrect password or username....!!!!!")
				print("\nPlease try again...!!!!")
				self.login()
		
			
					
#Making a library object
ges=Library(["Python","Basic C","C++ Advance","Data Structures","Machine Learning","Engineering Mathematics","Digital Electronics","HTML5","Core Java ","K-Map Basics","Encyclopedia","Artificial Intelligence","Nested Data Science"])

def main():
	print ("\n\nWELCOME TO THE LIBRARY OF GOKHALE EDUCATION SOCIETY'S R.H. SAPAT COLLEGE OF ENGINEERING , NASHIK\n")
	print("For Members Of The Library")
	print("  issue : To Issue the Book")
	print("  donate : To Donate the Book")
	print("  return : To Return the Book")
	print("  search : To search the book in Library")
	print("  exit : To come out of Library\n")
	
	print("Only For Authorized Users \n  lentdata : To get information about the Books Lending Database \n  delete book : To delete the Book in the Library \n  returndata : To get the information about the Books Return Database \n  delete member :  To delete the member of library\n")
	print("\nThe available books in the library are as follows : ")
	ges.display()
	print("")
	Exit=False
	while Exit is not True:
		UserInput=input("Enter Your Choice :  ")
		if UserInput=="issue":
			name_of_taker=input("Enter your name :  ")
			bookindex=int(input("Enter the number which is written at the left of the book :  "))
			bookname=ges.booklist[bookindex-1]
			ges.lend_book(name_of_taker,bookname,bookindex)
			print("")
			print("The available Books in the library : ")
			ges.display()
			print("")
		if UserInput=="return":
			name_return=input("Enter your name :  ")
			name_of_book=input("Enter the name of the book :  ")
			ges.return_book(name_return,name_of_book)
			print("")
			print("The available Books in the library : ")
			ges.display()
			print("")
		if UserInput=="lentdata":
			if prompt("Enter the Password :  ",is_password=True)=="gescoe":
				print("Authorization Granted......!!!!\n\nThe Lent Book Database is as follows......")
				ges.book_lent()
				print("\n")
				print("The available Books in the library : ")
				ges.display()
				print("")
			else:
				print("Access Denied.... \nNo Tresspassers are allowed.....")
				exit(0)
		if UserInput=="returndata":
			if prompt("Enter the Password :  ",is_password=True)=="gescoe":
				print("Authorization Granted......!!!!\n\nThe Returned Book Batabase is as follows.....")
				ges.book_return()
				print("\n")
				print("The available Books in the library : ")
				ges.display()
				print("")
			else:
				print("Access Denied.... \nNo Tresspassers are allowed.....")
				exit(0)
		if UserInput=="delete book":
			if prompt("Enter the Password :  ",is_password=True)=="gescoe":
				print("Authorization Granted......!!!!")
				bookindex=int(input("Enter the number of the book which you want to delete :  "))
				ges.delete_book(bookindex)
				print("")
				print("The available Books in the library : ")
				ges.display()
				print("")
			else:
				print("Access Denied... \nNo Tresspassers are allowed.....")
				exit(0)
		if UserInput=="delete member":
			if prompt("Enter the Password :  ",is_password=True)=="gescoe":
				print("Authorization Granted......!!!!")
				name=input("Enter the name of the member you want to delete : ")
				ges.delete_member(name)
				print("")
				print("The available Books in the library : ")
				ges.display()
				print("")
			else:
				print("Access Denied.... \nNo Tresspassers are allowed.....")
				exit(0)
		if UserInput=="donate":
			newbook=input("Enter the name of the Book :  ")
			ges.add_books(newbook)
			print("")
			print("The available Books in the library : ")
			ges.display()
			print("")
		if UserInput=="search":
			book_name=input("Enter the name of the Book you want to search :  ")
			ges.search_book(book_name)
			print("")
			ges.display()
			print("")
		if UserInput=="exit":
			print("")
			print("THANK YOU SO MUCH FOR VISITING TO OUR LIBRARY.......")
			Exit=True



the_visitor_input=input("Are you a member of library (Yes or No): ")
vi=the_visitor_input.lower()

if (vi=="no"):
		ges.register()		
elif (vi=="yes"):
		ges.login()
else:
		print("Please enter valid input....!!!!")