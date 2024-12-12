from peewee import Model
from models import User

class Gender(Model):
    def Count(self,gender) -> int:
        users = User.select().where(User.gender == '男' if gender == 0 else User.gender ==  '女')
        count = 0
        for user in users:
            count = count + 1
        return count