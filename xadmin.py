1. 配置settings.py
INSTALLED_APPS = ['xadmin','crispy_forms']

2. makemigrations, migeate

3. 在具体app下新建　adminx.py 用来管理xadmin功能和界面

4. adminx.py  注意：Rewrite UserAdmin的时候, 需要先把xadmin.plugins.auth里的site.register(User, UserAdmin)注释掉，取消默认注册；
              或者在adminx.py文件中加上 xadmin.site.unregister(UserProfile) 取消默认注册．

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'DSH Admin'
    site_footer = 'DSH Admin'
    menu_style = 'accordion'


class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'gender', 'address', 'mobile', 'image']
    search_fields = ['username', 'gender', 'address', 'mobile', 'image']
    list_filter = ['username', 'gender', 'address', 'mobile', 'image']


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
