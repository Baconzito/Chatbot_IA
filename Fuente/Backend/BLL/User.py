import MPP.User as MPus

class Bll_User:
    def __init__(self):
        self.MPus = MPus.Mpp_User()
        # Initialize any required attributes or services
        pass

    def new_user(self, user_data):
        # Logic to create a user
        pass

    def get_user(self, user_id):
        # Logic to get a user by ID
        pass

    def update_user(self, user_id, user_data):
        # Logic to update a user
        pass

    def delete_user(self, user_id):
        # Logic to delete a user
        pass

    def list_users(self):
        # Logic to list all users
        pass

    # Add any other methods that exist in Mpp_User