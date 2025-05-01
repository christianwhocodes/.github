from .models import WaksKevin


def base(request):
    return {"WaksKevin": WaksKevin.objects.first()}
