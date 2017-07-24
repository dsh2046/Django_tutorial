1．urls.py
from Admin_app.settings import MEDIA_ROOT

urlpatterns += url(r'^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT})

2. settings.py
TEMPLATES = [{'OPTIONS': {
                'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
                  'django.template.context_processors.media'  # 加上这一句(Django>=1.10)
            ],
        },}]
        
        
3. settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

4. Create 'media' directory

