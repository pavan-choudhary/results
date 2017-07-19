from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from pyexcel_xlsx import get_data
from django.views.generic.base import TemplateView
from .models import batch,semester
from django.http import JsonResponse ,HttpResponse

class IndexView(TemplateView):
	template_name='home.html'
	context_object_name='batches'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['batches'] = batch.objects.order_by('-batchy')
		return context

def getsems(request,batch_id):
	sems=semester.objects.filter(batchyear=batch_id).order_by('-sem').values_list('sem').distinct()
	return JsonResponse(list(sems),safe=False)

def result(request, **kwargs):
	if request.method == 'GET':
		yr=request.GET['y']
		b=request.GET['branch']
		s=request.GET['sem']

	yr=batch.objects.filter(id=yr).values('batchy')
	file=yr[0]['batchy']+"/"+b+"/"+s+".xlsx"
	credits=[4,4,1,4,1,4,1,4,1,2,4]
	value=0
	data = get_data(file)
	for x,y in data.items():
		for sno,sub in enumerate(y):
			total=0
			if sno>1:
				for sn,grade in enumerate(sub):
					if sn>2:
						if grade=='B+':
							value=7
						else:
							if grade=='A':
								value=8
							else:
								if grade=='B':
									value=6
								else:
									if grade=='A+':
										value=9
									else: 
										if grade=='O':
											value=10
										else: 
											if grade=='C':
												value=5
											else:
												if grade=='P':
													value=4
												else:
													if grade=='F':
														value=3
													else:
														if grade=='Ab':
															value=0
						total+=credits[sn-3] * value
			cgpa=round(total/30,2)
			data[x][sno].append(cgpa)
	info={'y':yr[0]['batchy'],'b':b,'s':s}
	return render(request,'result.html', {'result':data.items(),'info':info})




