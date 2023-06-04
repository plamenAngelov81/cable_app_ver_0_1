from django.contrib import admin

from cable_app_0_1.cable.models import Machine, Inductor, Cap, Clutch, Cable


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    pass


@admin.register(Inductor)
class InductorAdmin(admin.ModelAdmin):
    pass


@admin.register(Cap)
class CapAdmin(admin.ModelAdmin):
    pass


@admin.register(Clutch)
class ClutchAdmin(admin.ModelAdmin):
    pass


@admin.register(Cable)
class CableAdmin(admin.ModelAdmin):
    pass

