from django.contrib import admin
from app.models import NewsPost, RegisteredMember, Officer, Album, Picture

class NewsPostAdmin(admin.ModelAdmin):

    pass


class RegisteredMemberAdmin(admin.ModelAdmin):
	
    pass


class OfficerAdmin(admin.ModelAdmin):
	
    pass


class AlbumAdmin(admin.ModelAdmin):
	
    pass

class PictureAdmin(admin.ModelAdmin):
	
    pass

admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(RegisteredMember, RegisteredMemberAdmin)
admin.site.register(Officer, OfficerAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Picture, PictureAdmin)
