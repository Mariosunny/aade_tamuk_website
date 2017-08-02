from django.contrib import admin
from app.models import NewPost, RegisteredMember, Officer

class NewPostAdmin(admin.ModelAdmin):

    pass


class RegisteredMemberAdmin(admin.ModelAdmin):
	
    pass


class OfficerAdmin(admin.ModelAdmin):
	
    pass


admin.site.register(NewPost, NewPostAdmin)
admin.site.register(RegisteredMember, RegisteredMemberAdmin)
admin.site.register(Officer, OfficerAdmin)
