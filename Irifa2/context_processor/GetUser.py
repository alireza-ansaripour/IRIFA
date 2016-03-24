from persons.models import Expert, NGO


def getUser(request):
    expert = None
    if request.user.is_authenticated() and not request.user.is_superuser:
        experts = Expert.objects.all()
        for ex in experts:
            if ex.person.username == request.user.username:
                expert = ex
    return {
        'expert': expert
    }


def getNgo(request):
    list = {"NORTH_AMERICA": [], "SOUTH_AMERICA": [], "EUROPE": [], "AFRICA": [], "AUSTRALIA": []}
    ngos = NGO.objects.filter(continent='ASIA')
    print(ngos)
    return {
        'north_america': NGO.objects.filter(continent="NORTH_AMERICA"),
        'south_america': NGO.objects.filter(continent="SOUTH_AMERICA"),
        'europe': NGO.objects.filter(continent="EUROPE"),
        'africa': NGO.objects.filter(continent="AFRICA"),
        'australia': NGO.objects.filter(continent="AUSTRALIA"),
        'asia': NGO.objects.filter(continent='ASIA'),
    }