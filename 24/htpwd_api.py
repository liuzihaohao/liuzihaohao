import os
from passlib.apache import HtpasswdFile

class HtpasswdManager:
    def __init__(self, htpasswd_file='/etc/nginx/.htpasswd'):
        self.htpasswd_file = htpasswd_file
        # 如果文件不存在，创建它
        if not os.path.exists(self.htpasswd_file):
            with open(self.htpasswd_file, 'w') as f:
                pass
        self.htpasswd = HtpasswdFile(self.htpasswd_file, new=True)

    def add_user(self, username, password):
        """ 添加用户到 .htpasswd 文件 """
        if self.htpasswd.get_hash(username):
            raise ValueError(f"User '{username}' already exists.")
        hashed_password = self.htpasswd.hash(password)
        self.htpasswd.set_password(username, hashed_password)
        self.htpasswd.save()
        print(f"User '{username}' added successfully.")

    def remove_user(self, username):
        """ 从 .htpasswd 文件中删除用户 """
        if not self.htpasswd.get_hash(username):
            raise ValueError(f"User '{username}' does not exist.")
        self.htpasswd.delete(username)
        self.htpasswd.save()
        print(f"User '{username}' removed successfully.")

    def list_users(self):
        """ 列出所有用户 """
        users = self.htpasswd.users()
        if not users:
            print("No users found.")
        else:
            print("Users in .htpasswd file:")
            for user in users:
                print(user)

    def update_password(self, username, new_password):
        """ 更新用户密码 """
        if not self.htpasswd.get_hash(username):
            raise ValueError(f"User '{username}' does not exist.")
        hashed_password = self.htpasswd.hash(new_password)
        self.htpasswd.set_password(username, hashed_password)
        self.htpasswd.save()
        print(f"Password for user '{username}' updated successfully.")
