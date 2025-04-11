# src/services/linking_service.py

class LinkingService:
    def __init__(self):
        # This could be a database connection or any other setup needed
        self.linked_data = {}

    def link_customer_to_project(self, customer_id: int, project_id: int) -> str:
        """
        Links a customer to a project.

        :param customer_id: ID of the customer
        :param project_id: ID of the project
        :return: Success message
        """
        if customer_id in self.linked_data:
            self.linked_data[customer_id].add(project_id)
        else:
            self.linked_data[customer_id] = {project_id}
        return f"Customer {customer_id} linked to project {project_id}"

    def unlink_customer_from_project(self, customer_id: int, project_id: int) -> str:
        """
        Unlinks a customer from a project.

        :param customer_id: ID of the customer
        :param project_id: ID of the project
        :return: Success message
        """
        if customer_id in self.linked_data and project_id in self.linked_data[customer_id]:
            self.linked_data[customer_id].remove(project_id)
            if not self.linked_data[customer_id]:
                del self.linked_data[customer_id]
            return f"Customer {customer_id} unlinked from project {project_id}"
        return f"Customer {customer_id} was not linked to project {project_id}"