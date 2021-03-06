from trainmefitapp.models import *
from django.http import HttpResponse
import json
import pdb

def get_customer_list(request):
##    pdb.set_trace()
    try:
        
        print 'Customer List '
        customer_list = UserProfile.objects.all()
        user_list = []
        for customer in customer_list:
            if customer.user_row_status == 1 :
                status = '<span class="label label-success">Active</span>'
            else:
                status = '<span class="label label-warning">Inactive</span>'
            
            edit = '<a href="/user-detail-page/" class="table-link"> '+ '<span class="fa-stack">' + '<i class="fa fa-square fa-stack-2x"></i> <i class="fa fa-pencil fa-stack-1x fa-inverse"></i> </span> </a>'
            
            temp_obj= {
                'user_full_name': customer.user_full_name,
                'objective': customer. user_objective,
                'creation_date':customer.creation_date.strftime('%d-%m-%Y'),
                'email': customer.email,
                'status': status,
                'edit' : edit
             
            }
            user_list.append(temp_obj)
        data = {'data': user_list}
    except Exception, e:
        print 'Exception : ', e
        data = {'data':'none'}
    return HttpResponse(json.dumps(data), content_type='application/json')    