from django.db import models

class Tm_User(models.Model):
    Id_User = models.CharField(primary_key=True, blank=False, null=False , max_length=20)
    No_Celu = models.CharField(blank=False, null=True, max_length=50)

    class Meta:
        verbose_name = "Tm_User"
        verbose_name_plural = "Tm_Users"

    def __str__(self):
        return Id_User

class Td_User_Cont(models.Model):
    Id_Cont = models.CharField(primary_key=True, blank=False, null=False, max_length=20)
    Id_User = models.ForeignKey(Tm_User, blank=False, null=False, max_length=20)
    Co_Nomb = models.CharField(blank=False, null=True, max_length=50)
    class Meta:
        verbose_name = "Td_User_Cont"
        verbose_name_plural = "Td_User_Conts"

    def __str__(self):
        return Id_Cont

class Td_User_Llam(models.Model):
    Id_User = models.ForeignKey(Tm_User, blank=False, null=False, max_length=20)
    Ll_Cont_Nomb = models.CharField(blank=False, null=True, max_length=50)
    Ll_Cont_Celu = models.CharField(blank=False, null=False, max_length=20)
    Ll_Fech = models.DateField(blank=False, null=False)
    Ll_Tiem_Dura = models.TimeField(blank=False, null=False)
    Ll_Tipo = models.CharField(blank=False, null=False, max_length=10)
    class Meta:
        verbose_name = "Td_User_Llam"
        verbose_name_plural = "Td_User_Llams"

    def __str__(self):
        return Ll_Cont_Nomb
