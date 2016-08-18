from django.contrib import admin
from .models import Tm_User, Td_User_Cont, Td_User_Llam, Td_User_Apli

@admin.register(Tm_User)

class adminUser(admin.ModelAdmin):
    list_display = ('Id_User', 'No_Celu')
    lis_filter = ('Id_User')

@admin.register(Td_User_Cont)

class adminContactos(admin.ModelAdmin):
    list_display = ('Id_Cont', 'Id_User', 'Co_Nomb')
    lis_filter = ('Id_User')

@admin.register(Td_User_Llam)

class adminLlamadas(admin.ModelAdmin):
    list_display = ('Id_User', 'Ll_Cont_Nomb', 'Ll_Cont_Celu', 'Ll_Fech', 'Ll_Tiem_Dura', 'Ll_Tipo')
    lis_filter = ('Id_User')

@admin.register(Td_User_Apli)

class adminAplicaciones(admin.ModelAdmin):
    list_display = ('Id_User', 'Ap_Nomb', 'Ap_Tiem', 'Ap_Uso_Bate', 'Ap_Dato_Reci', 'Ap_Dato_Envi', 'Ap_Fech')
    lis_filter = ('Id_User')
