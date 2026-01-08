
from datetime import datetime


members = {}
audit_logs =[]

def log_audit(action, entity_type, entity_id, performed_by):
    audit_logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "performed_by": performed_by
    })


class member:


    def add_member():
        member_id = input("Enter Member ID: ")
        name = input("Enter Full Name: ")
        phone = input("Enter Phone Number: ")
        mtype = input("Membership Type (STUDENT/GENERAL): ").upper()

        if mtype not in ["STUDENT", "GENERAL"]:
            print("Invalid membership type.")
            return

        members[member_id] = {
            "name": name,
            "phone": phone,
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "type": mtype,
            "status": "ACTIVE"
        }

        log_audit("ADD_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member added successfully.")

    
    def suspend_member():
        member_id = input("Enter Member ID: ")

        if member_id not in members:
            print("Member not found.")
            return

        members[member_id]["status"] = "SUSPENDED"
        log_audit("SUSPEND_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member suspended.")


    def suspend_member():
        member_id = input("Enter Member ID: ")

        if member_id not in members:
            print("Member not found")
            return
        
        members[member_id] = "SUSPENDED"
        log_audit("SUSPEND_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member suspended")


    def activate_member():
        member_id = input("ENter Member ID: ") 

        if member_id not in members:
            print("Member not found")   
            return
        
        member = "ACTIVE"
        log_audit("ACTIVATE_MEMBER", "MEMBER",member_id, "Librarian")
        print("Member activated")
    

    def deactivate_member():
        member_id = input("Enter Member ID: ")

        if member_id not in members:
            print("Member not found")
            return
        
        members = "INACTIVE"
        log_audit("DEACTIVATE_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member marked as INACTIVE")

        
add_member()

