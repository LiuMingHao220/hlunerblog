from xadmin import views
import xadmin


class GlobalSettings(object):
    site_title = '博客后台管理系统' # 修改页眉
    site_footer = 'hluner'  # 修改页脚
    menu_style = 'accordion'  #修改菜单栏 改成收缩样式


class BaseSetting(object):
    enable_themes = True   # 开启主题使用
    use_bootswatch = True  # 开启主题选择  (不过我并没有发现主题列表)



xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)