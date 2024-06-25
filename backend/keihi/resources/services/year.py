from resources.models import Year


class YearServices:
    def get_all():
        return Year.objects.all()
