import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='invoice_audit.log',
                    filemode='a')

def log_invoice_generation(invoice_id, project_id, total_amount, due_date):
    logging.info(f"Invoice {invoice_id} for project {project_id} generated with total amount {total_amount} due on {due_date}.")

def log_invoice_adjustment(invoice_id, adjustment_details):
    logging.info(f"Invoice {invoice_id} adjusted with details: {adjustment_details}.")

def log_invoice_notification(invoice_id, stakeholders):
    logging.info(f"Notification sent for invoice {invoice_id} to stakeholders: {', '.join(stakeholders)}.")
