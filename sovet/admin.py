from django.contrib import admin
from .models import GeneralInfo, Garanty, Goals, Docs, ServiceBlock, ServiceSection

admin.site.register(GeneralInfo)
admin.site.register(Garanty)
admin.site.register(Goals)
admin.site.register(Docs)
admin.site.register(ServiceBlock)
admin.site.register(ServiceSection)
