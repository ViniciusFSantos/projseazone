from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
import uuid

class Base(models.Model):
    criado_em = models.DateTimeField('Criado em:', auto_now_add=True)
    atualizado_em = models.DateTimeField('Atualizado em:', auto_now=True)
    
    class Meta:
        abstract = True    

class Imoveis(Base):
    imovel_codigo = models.CharField(blank=False, max_length=10, validators=[RegexValidator(r'^\d{1,999999}$')], unique=True)
    limite_hospedes = models.CharField(blank=False, max_length=1, validators=[RegexValidator(r'^\d{1,5}$')])
    banheiros_quant = models.CharField(blank=False, max_length=1, validators=[RegexValidator(r'^\d{1,4}$')])
    permite_animais =  models.BooleanField(blank=False, default=False)
    valor_limpeza = models.DecimalField(max_digits=6, decimal_places=2, blank=False, validators=[MinValueValidator(1)])
    data_ativa = models.DateField(auto_now_add=False, blank=False)

    def __str__(self):
        return self.imovel_codigo
    
    class Meta:
        verbose_name_plural = "Imóveis"
    
class Anuncios(Base):
    anuncio_imovel = models.ForeignKey(Imoveis, on_delete=models.DO_NOTHING)
    plataforma = models.CharField(max_length=10, blank=False)
    taxa_cobrada = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(1)], blank=False)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name_plural = "Anúncios"
    
class Reservas(Base):
    reserva_anuncio = models.ForeignKey(Anuncios, on_delete=models.DO_NOTHING)
    reserva_codigo = models.UUIDField(primary_key='True', default=uuid.uuid1, editable='False', unique=True)
    chekin_data = models.DateField(auto_now_add=False, blank=False)
    chekout_data = models.DateField(auto_now_add=False, blank=False)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, blank=False, validators=[MinValueValidator(1)])
    quant_hospedes = models.CharField(blank=False, max_length=5, validators=[RegexValidator(r'^\d{1,5}$')])
    comentarios = models.TextField(max_length=120, blank=True)
    
    def __str__(self):
        return str(self.reserva_codigo)
    
    class Meta:
        verbose_name_plural = "Reservas"