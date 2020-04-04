from bot.models import Profile


def get_profile_count():
    count = Profile.objects.count()
    return count
