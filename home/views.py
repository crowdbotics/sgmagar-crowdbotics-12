from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'aa_stripe', 'url': 'http://pypi.python.org/pypi/aa_stripe/0.4.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-12',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
