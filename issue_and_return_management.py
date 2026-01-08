
from datetime import datetime, timedelta

issues = {}


def log_audit(action, entity_type, entity_id, performed_by):
    audit_logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "performed_by": performed_by
    })

class issue_return:

    def issue_book():
        issue_id = f"I{len(issues) + 1}"
        book_id = input("Book ID: ")
        member_id = input("Member ID: ")

        if book_id not in books or member_id not in members:
            print("Invalid Book or Member ID.")
            return

        if books[book_id]["status"] != "ACTIVE" or books[book_id]["available"] == 0:
            print("Book cannot be issued.")
            return

        if members[member_id]["status"] != "ACTIVE":
            print("Member cannot issue books.")
            return

        issued = sum(
            1 for i in issues.values()
            if i["member_id"] == member_id and i["return_date"] is None
        )

        limit = 2 if members[member_id]["type"] == "STUDENT" else 3
        if issued >= limit:
            print("Issue limit exceeded.")
            return

        issues[issue_id] = {
            "book_id": book_id,
            "member_id": member_id,
            "issue_date": datetime.now(),
            "due_date": datetime.now() + timedelta(days=14),
            "return_date": None
        }

        books[book_id]["available"] -= 1
        print("Book issued successfully.")


def return_book():
    issue_id = input("Issue ID: ")

    if issue_id not in issues:
        print("Invalid Issue ID.")
        return

    if issues[issue_id]["return_date"] is not None:
        print("Book already returned.")
        return

    issues[issue_id]["return_date"] = datetime.now()
    books[issues[issue_id]["book_id"]]["available"] += 1

    if issues[issue_id]["return_date"] > issues[issue_id]["due_date"]:
        print("Late return.")

    print("Book returned successfully.")


        