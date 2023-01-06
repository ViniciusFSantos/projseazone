from django.contrib import admin
from core.models import Imoveis, Anuncios, Reservas

@admin.register(Imoveis)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('imovel_codigo', 'limite_hospedes','banheiros_quant','permite_animais','valor_limpeza','data_ativa')

@admin.register(Anuncios)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('anuncio_imovel','plataforma', 'taxa_cobrada' )

@admin.register(Reservas)
class StatusChamadoAdmin(admin.ModelAdmin):
    list_display = ('reserva_anuncio','reserva_codigo', 'chekin_data','chekout_data','valor_total','quant_hospedes','comentarios')

    