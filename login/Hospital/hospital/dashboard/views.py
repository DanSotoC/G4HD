from django.shortcuts import render

def home(request):
	#pacientes = Usuario.objects.count()
	context = {

	}
	return render(request,"dashboard.html", context)
