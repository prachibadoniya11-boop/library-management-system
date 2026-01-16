
from datetime import datetime, timedelta


class IssueReturn_management:
    def __init__(self,books,members):
        self.books = books
        self.members = members
        self.issues = {}
        self.audit_logs = []

    def log_audit(self, action, entity_type, entity_id, performed_by):
        self.audit_logs.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "performed_by": performed_by
        })


    def issue_book(self):
        issue_id = f"I{len(self.issues) + 1}"
        book_id = input("Book ID: ")
        member_id = input("Member ID: ")

        if book_id not in self.books or member_id not in self.members:
            print("Invalid Book or Member ID.")
            return

        if self.books[book_id]["status"] != "ACTIVE" or self.books[book_id]["available"] == 0:
            print("Book cannot be issued.")
            return

        if self.members[member_id]["status"] != "ACTIVE":
            print("Member cannot issue books.")
            return

        issued = sum(
            1 for i in self.issues.values()
            if i["member_id"] == member_id and i["return_date"] is None
        )

        limit = 2 if self.members[member_id]["type"] == "STUDENT" else 3
        if issued >= limit:
            print("Issue limit exceeded.")
            return

        self.issues[issue_id] = {
            "book_id": book_id,
            "member_id": member_id,
            "issue_date": datetime.now(),
            "due_date": datetime.now() + timedelta(days=14),
            "return_date": None
        }

        self.books[book_id]["available"] -= 1
        self.log_audit("ISSUE_BOOK", "ISSUE", issue_id, "Librarian")
        print("Book issued successfully.")


    def return_book(self):
        issue_id = input("Issue ID: ")

        if issue_id not in self.issues:
            print("Invalid Issue ID.")
            return

        if self.issues[issue_id]["return_date"] is not None:
            print("Book already returned.")
            return

        self.issues[issue_id]["return_date"] = datetime.now()
        self.books[self.issues[issue_id]["book_id"]]["available"] += 1

        if self.issues[issue_id]["return_date"] > self.issues[issue_id]["due_date"]:
            print("Late return.")

        print("Book returned successfully.")

obj = IssueReturn_management('books','members')
obj.issue_book()

        