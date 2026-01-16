
from datetime import datetime

class Member_management:
    def __init__(self):
        self.members = {}
        self.audit_logs = []


    def log_audit(self,action, entity_type, entity_id, performed_by):
            self.audit_logs.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "action": action,
                "entity_type": entity_type,
                "entity_id": entity_id,
                "performed_by": performed_by
            })


    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Full Name: ")
        phone = input("Enter Phone Number: ")
        mtype = input("Membership Type (STUDENT/GENERAL): ").upper()

        if mtype not in ["STUDENT", "GENERAL"]:
            print("Invalid membership type.")
            return

        self.members[member_id] = {
            "name": name,
            "phone": phone,
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "type": mtype,
            "status": "ACTIVE"
        }

        self.log_audit("ADD_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member added successfully.")

    
    def suspend_member(self):
        member_id = input("Enter Member ID: ")

        if member_id not in self.members:
            print("Member not found.")
            return

        self.members[member_id]["status"] = "SUSPENDED"
        self.log_audit("SUSPEND_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member suspended.")


    
    def activate_member(self):
        member_id = input("ENter Member ID: ") 

        if member_id not in self.members:
            print("Member not found")   
            return
        
        self.member = "ACTIVE"
        self.log_audit("ACTIVATE_MEMBER", "MEMBER",member_id, "Librarian")
        print("Member activated")
    

    def deactivate_member(self):
        member_id = input("Enter Member ID: ")

        if member_id not in self.members:
            print("Member not found")
            return
        
        self.members = "INACTIVE"
        self.log_audit("DEACTIVATE_MEMBER", "MEMBER", member_id, "Librarian")
        print("Member marked as INACTIVE")

        

obj = Member_management()
obj.add_member()
obj.print_member()

