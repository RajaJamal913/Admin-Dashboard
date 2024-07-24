from django.contrib import admin
from .models import Staff,ActivityLog,User,Order,BannedIP,API,PanelRate,OrderPanelConfig



admin.site.register(User)
admin.site.register(Order)
admin.site.register(BannedIP)
admin.site.register(Staff)
admin.site.register(ActivityLog)
admin.site.register(API)
admin.site.register(PanelRate)
admin.site.register(OrderPanelConfig)

