from datetime import datetime
def log_audit(action, entity_type, entity_id, performed_by):
    audit_logs.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "action": action,
        "entity_type": entity_type,
        "entity_id": entity_id,
        "performed_by": performed_by
    })


var = 4
