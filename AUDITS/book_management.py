from datetime import datetime

class Bookmanager:
    def __inti__(self):
        self.books = {}
        self.audit_logs = []



    def log_audit(self,action, entity_type, entity_id, performed_by):
        self.audit_logs.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "performed_by": performed_by
        })



    

    def add_book(self, book_id, title, author, category, year, total):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        category = input("Enter Category: ")
        year = int(input("Enter Year of Publication: "))
        total = int(input("Enter Total Copies: "))

        self.books [book_id] = {
            "title": title,
            "author": author,
            "category": category,
            "year": year,
            "total": total,
            "available": total,
            "status": "ACTIVE"
        }

    def update_book_copies(self):
        book_id = input("Enter book ID: ") 

        if book_id not in self.books:
            print("Book not found")
            return
        new_total = int(input("Enter new total copies: "))

        issued = self.books[book_id]["total"] - self.books[book_id]["available"]

        if new_total < issued :
            print("Cannot set total copies less than issued copies")
            return
        
        self.books[book_id]["total"] = new_total
        self.books[book_id] ["available"] = new_total - issued
        self.log_audit("UPDATED_COPIES", "BOOK", book_id, "Librarian")

        print("Book copies updated successfully")    

    def mark_book_damaged(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found")
            return
            
        self.books[book_id]["status"] = "DAMAGED" 
        self.log_audit("MARK_DAMAGED", "BOOK", book_id, "Librarian")
        print("Book marked as damaged") 
    

    def remove_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found")
            return
        
        if self.books[book_id]["available"] != self.books[book_id]["total"]:
            print("Cannot remove book.copies are still issued")
            return

        self.books[book_id]["status"] = "REMOVED"
        self.log_audit("REMOVE_BOOK","BOOK", book_id,"Librarian")
        print("Book marked as REMOVED")

  
obj = Bookmanager()
obj.add_book()
obj.print_books
