import logging

logger = logging.getLogger(__name__)

class LinkingLoggingMiddleware:
    def log_linking_action(self, action: str, customer_id: int, project_id: int):
        logger.info(f"{action} - Customer ID: {customer_id}, Project ID: {project_id}")
