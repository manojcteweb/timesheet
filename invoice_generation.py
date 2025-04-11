from datetime import datetime

class Invoice:
    def __init__(self, invoice_id, project_id, total_amount, due_date, items):
        self.invoice_id = invoice_id
        self.project_id = project_id
        self.total_amount = total_amount
        self.due_date = due_date
        self.items = items

    def generate_invoice(self):
        # Logic to generate invoice
        print(f"Invoice {self.invoice_id} for project {self.project_id} generated.")
        print(f"Total Amount: {self.total_amount}")
        print(f"Due Date: {self.due_date}")
        print("Items:")
        for item in self.items:
            print(f"- {item}")

    def format_for_accounting_software(self):
        # Logic to format invoice for accounting software
        formatted_invoice = {
            'invoice_id': self.invoice_id,
            'project_id': self.project_id,
            'total_amount': self.total_amount,
            'due_date': self.due_date,
            'items': self.items
        }
        print(f"Formatted invoice for accounting software: {formatted_invoice}")
        return formatted_invoice

    def allow_manual_adjustments(self, adjustments):
        # Logic to allow manual adjustments to the invoice
        print(f"Applying manual adjustments: {adjustments}")
        for adjustment in adjustments:
            self.total_amount += adjustment['amount']
            self.items.append(adjustment['description'])
        print(f"Adjusted Total Amount: {self.total_amount}")
        print("Updated Items:")
        for item in self.items:
            print(f"- {item}")