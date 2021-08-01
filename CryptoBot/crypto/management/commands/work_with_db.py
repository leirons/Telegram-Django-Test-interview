from crypto.models import UserProfile
from asgiref.sync import sync_to_async

from .exception import CantCreateUserProfile


def check_if_user_created(request):
    """Проверяем пользователя на наличие"""
    if UserProfile.objects.get(user_id=request):
        return True
    return False


@sync_to_async
def create_user_profile(request, name, surname):
    """Создаем пользователя"""
    if not check_if_user_created(request=request):
        if surname == None:
            surname = 'None'
        elif name == None:
            name = 'None'
        try:
            profile = UserProfile.objects.create(user_id=request, name=name, surname=surname)
        except:
            raise CantCreateUserProfile
        profile.save()
