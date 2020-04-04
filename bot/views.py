from bot.models import Profile


def get_profiles():
    profile_names = Profile.objects.all().values_list("name", flat=True)
    return profile_names
