class Notification:
    def __init__(self, stakeholders):
        self.stakeholders = stakeholders

    def send_invoice_notification(self, invoice_id, project_id, total_amount, due_date):
        # Logic to send notification to stakeholders
        for stakeholder in self.stakeholders:
            print(f"Notification sent to {stakeholder}: Invoice {invoice_id} for project {project_id} with amount {total_amount} is due on {due_date}.")

# Example usage:
# stakeholders = ['stakeholder1@example.com', 'stakeholder2@example.com']
# notification = Notification(stakeholders)
# notification.send_invoice_notification('INV123', 'PROJ456', 1500.00, '2023-12-31')