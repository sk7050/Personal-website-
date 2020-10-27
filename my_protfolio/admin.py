from django.contrib import admin
from .models import Sk_home
from .models import Sk_about,Sk_cv,Sk_certificate,Sk_online_course,Interest_Cata,Sk_Interest,Project_Cata,Project
admin.site.register(Sk_home)
admin.site.register(Sk_about)
admin.site.register(Sk_cv)
admin.site.register(Sk_certificate)
admin.site.register(Sk_online_course)
admin.site.register(Interest_Cata)
admin.site.register(Sk_Interest)
admin.site.register(Project_Cata)
admin.site.register(Project)
# Register your models here.
