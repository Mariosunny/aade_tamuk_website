from django.contrib import admin
from app.models import NewsPost, RegisteredMember, Officer

class NewsPostAdmin(admin.ModelAdmin):

    pass


class RegisteredMemberAdmin(admin.ModelAdmin):
	
    pass


class OfficerAdmin(admin.ModelAdmin):
	
    pass


admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(RegisteredMember, RegisteredMemberAdmin)
admin.site.register(Officer, OfficerAdmin)
