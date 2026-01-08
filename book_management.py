from datetime import datetime

books = {}
audit_logs = []

def log_audit(action, entity_type, entity_id, performed_by):
    audit_logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "performed_by": performed_by
    })


class Bookmanager:
    

    def add_book():
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        category = input("Enter Category: ")
        year = int(input("Enter Year of Publication: "))
        total = int(input("Enter Total Copies: "))

        books [book_id] = {
            "title": title,
            "author": author,
            "category": category,
            "year": year,
            "total": total,
            "available": total,
            "status": "ACTIVE"
        }

    def update_book_copies():
        book_id = input("Enter book ID: ") 

        if book_id not in books:
            print("Book not found")
            return
        new_total = int(input("Enter new total copies: "))

        issued = books[book_id]["total"] - books[book_id]["available"]

        if new_total < issued :
            print("Cannot set total copies less than issued copies")
            return
        books[book_id]["total"] = new_total
        books[book_id] ["available"] = new_total - issued

        print("Book copies updated successfully")    

    def mark_book_damaged():
        book_id = input("Enter Book ID: ")

        if book_id not in books:
            print("Book not found")
            return
        
        books[book_id]["status"] = "DAMAGED" 
        log_audit("MARK_DAMAGED", "BOOK", book_id, "Librarian")
        print("Book marked as damaged") 
  

    def remove_book():
        book_id = input("Enter Book ID: ")

        if book_id not in books:
            print("Book not found")
            return
        if books[book_id]["available"] != books[book_id]["total"]:
            print("Cannot remove book.copies are still issued")
            return

        books[book_id]["status"] = "REMOVED"
        log_audit("REMOVE_BOOK","BOOK", book_id,"Librarian")
        print("Book marked as REMOVED")

    
    add_book()                           
          

