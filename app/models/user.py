
class User():

    @classmethod
    def get(self):
        user_list = []
        for user in users:
            data = {}
            data['first_name'] = user['first_name']
            data['last_name'] =  user['last_name']
            user_list.append(data)
        return user_list
