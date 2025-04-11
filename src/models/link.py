class Link:
    def __init__(self, customer_id: int, project_id: int):
        self.customer_id = customer_id
        self.project_id = project_id

    def create_link(self) -> dict:
        """
        Creates a link between a customer and a project.

        :return: A dictionary representing the link.
        """
        return {
            "customer_id": self.customer_id,
            "project_id": self.project_id
        }

    def get_link_data(self) -> dict:
        """
        Retrieves the link data as a dictionary.

        :return: A dictionary containing link data.
        """
        return {
            "customer_id": self.customer_id,
            "project_id": self.project_id
        }