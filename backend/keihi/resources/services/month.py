from resources.models import Month


class MonthServices:
    def get_all():
        return Month.objects.get()
        