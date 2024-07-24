# admin_dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User,Order,BannedIP,ActivityLog,Staff,API
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PanelRate
from .forms import PanelRateForm



def user_list(request):
    users = User.objects.all() 
    return render(request, 'templates/user_list.html', {'users': users})
# admin_dashboard/views.py

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'templates/order_list.html', {'orders': orders})

# admin_dashboard/views.py

def ip_banning(request):
    banned_ips = BannedIP.objects.all()
    return render(request, 'templates/Ip_Banning.html', {'banned_ips': banned_ips})

# admin_dashboard/views.py

def activity_logs(request):
    logs = ActivityLog.objects.all()
    return render(request, 'templates/activity_logs.html', {'logs': logs})

# admin_dashboard/views.py

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'templates/staff_list.html', {'staff_members': staff_members})

def overview(request):
    return render(request, 'templates/overview.html')
from .models import API


def api_management(request):
    apis = API.objects.all()
    return render(request, 'templates/api_management.html', {'apis': apis})


def toggle_api_status(request, api_id):
    api = get_object_or_404(API, id=api_id)
    api.status = not api.status
    api.save()
    return redirect('admin_dashboard:api_management')


def delete_api(request, api_id):
    api = get_object_or_404(API, id=api_id)
    api.delete()
    return redirect('admin_dashboard:api_management')


def add_duplicate_api(request):
    if request.method == 'POST':
        domain = request.POST['domain']
        status = request.POST.get('status', False)
        API.objects.create(domain=domain, status=status)
        return redirect('admin_dashboard:api_management')
    return render(request, 'templates/api_management.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import PanelRate,OrderPanelConfig

def panel_rate_management(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('rate_'):
                user_id = key.split('_')[1]
                try:
                    user = User.objects.get(pk=user_id)
                    rate, created = PanelRate.objects.get_or_create(user=user)
                    rate.rate = value
                    rate.save()
                except User.DoesNotExist:
                    continue  # Skip if the user does not exist
        return redirect('admin_dashboard:panel_rate_management')

    users = User.objects.all()
    return render(request, 'templates/panel_rate_management.html', {'users': users})

@login_required
def order_panel_configuration(request):
    if request.method == 'POST':
        default_features = request.POST.get('default_features') == 'on'
        maintenance_mode = request.POST.get('maintenance_mode') == 'on'
        custom_message = request.POST.get('custom_message')

        config, created = OrderPanelConfig.objects.get_or_create(id=1)  # Assuming there's only one config
        config.default_features = default_features
        config.maintenance_mode = maintenance_mode
        config.custom_message = custom_message
        config.save()

        return redirect('admin_dashboard:order_panel_configuration')

    config = OrderPanelConfig.objects.first()
    return render(request, 'templates/order_panel_configuration.html', {'config': config})