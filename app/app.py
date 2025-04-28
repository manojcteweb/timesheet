```python
from datetime import datetime
import json

class AuditTrail:
    def __init__(self):
        self.logs = []
        self.admin_users = set()
    
    def log_activity(self, user_id, action):
        timestamp = datetime.now().isoformat()
        self.logs.append({'timestamp': timestamp, 'user_id': user_id, 'action': action})
    
    def add_admin_user(self, user_id):
        self.admin_users.add(user_id)
    
    def get_logs(self, user_id, filters=None):
        if user_id not in self.admin_users:
            raise PermissionError("Access denied")
        
        filtered_logs = self.logs
        if filters:
            if 'date' in filters:
                filtered_logs = [log for log in filtered_logs if log['timestamp'].startswith(filters['date'])]
            if 'user' in filters:
                filtered_logs = [log for log in filtered_logs if log['user_id'] == filters['user']]
            if 'action' in filters:
                filtered_logs = [log for log in filtered_logs if log['action'] == filters['action']]
        
        return filtered_logs

    def save_logs(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.logs, f, indent=4)

    def load_logs(self, filepath):
        with open(filepath, 'r') as f:
            self.logs = json.load(f)

# Example usage
audit_trail = AuditTrail()
audit_trail.add_admin_user('admin1')
audit_trail.log_activity('user1', 'login')
audit_trail.log_activity('user2', 'create_project')
logs = audit_trail.get_logs('admin1', filters={'action': 'login'})
audit_trail.save_logs('audit_logs.json')
```