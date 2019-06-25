from django.contrib import admin

# Register your models here.
from  .models import weihu,yonghu,feiyong
class weihu_admin(admin.ModelAdmin):
    list_display = ['weihu_id','time','money','zhuangtai','news','stl','weixiudan_id_id','yuangong_id_id']
admin.site.register(weihu,weihu_admin)
class yonghu_admin(admin.ModelAdmin):
    list_display = ['id','name','type','password','money','tele','live','delt']
admin.site.register(yonghu,yonghu_admin)
class feiyong_admin(admin.ModelAdmin):
    list_display = ['yonghu_id','feiyong_danhaoid','feiyong_kaishi','feiyong_jieshu','feiyong_leixing','feiyong_qian','feiyong_zhuangtai','feiyong_company']
admin.site.register(feiyong,feiyong_admin)