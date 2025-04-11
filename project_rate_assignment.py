class ProjectRateAssignment:
    def __init__(self):
        self.role_rates = {}

    def set_rate_for_role(self, role, rate):
        """
        Set the rate for a specific role.
        :param role: The role for which the rate is being set.
        :param rate: The rate to be set for the role.
        """
        self.role_rates[role] = rate
        print(f"Rate for role '{role}' set to {rate}.")

    def get_rate_for_role(self, role):
        """
        Retrieve the rate for a specific role.
        :param role: The role for which the rate is being retrieved.
        :return: The rate for the role, or None if not set.
        """
        return self.role_rates.get(role, None)