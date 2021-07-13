from os import getenv


def export_vars(request):
    data = {}
    data['LOGO'] = getenv('LOGO')
    return data
