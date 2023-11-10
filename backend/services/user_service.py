from models.user import User
from repository.user_repository import UserRepository
from services.base_service import BaseService


class UserService(BaseService):
    _repo = UserRepository()

    def add_user(self, username: str, age: int, display_name: str, password: str, profile_picture: str, rating: float,
                 about: str, interests: str, tags: str, activities_created: str, activities_enrolled: str,
                 activities_completed: str, friends: str):
        user = self.parse_user(username, age, display_name, password, profile_picture, rating, about, interests, tags,
                               activities_created, activities_enrolled, activities_completed, friends)
        return self._repo.add(user)

    def remove_user(self, column, value):
        return self._repo.remove(column, value)

    def update_user(self, column, value, **kwargs):
        return self._repo.update(column, value, **kwargs)

    def get_user(self, username):
        return self._repo.get_by_username(username)

    def get_all_users(self):
        return self._repo.get_all()

    def parse_user(self, username: str, age: int, display_name: str, password: str, profile_picture: str, rating: float,
                   about: str, interests: str, tags: str, activities_created: str, activities_enrolled: str,
                   activities_completed: str, friends: str):
        return User(username=username, age=age, display_name=display_name, password=password,
                    profile_picture=profile_picture, rating=rating, about=about, interests=interests, tags=tags,
                    activities_created=activities_created, activities_enrolled=activities_enrolled,
                    activities_completed=activities_completed, friends=friends)
