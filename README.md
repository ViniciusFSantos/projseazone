# Nome do Projeto: 
Khanto

# Objetivos do projeto:
Projeto desenvolvido para teste de conhecimentos solicitado pela empresa Seazone. Visando alcançar a vaga de Desenvolvedor Python.

# Test Case:
Envolve a criação de 3 APIs

A empresa Khanto começou a desenvolver um novo sistema e precisa criar um banco de dados com 3 entidades: Imóveis, Anúncios e Reservas. Um imóvel pode ter diversos anúncios, mas um anúncio é referente apenas a um imóvel. Um anúncio pode ter várias reservas, mas uma reserva se refere a apenas um anúncio.
A tabela de imóveis deve conter: o código do imóvel, o limite de hóspedes, a quantidade de banheiros, se aceita animais de estimação, o valor de limpeza, a data de ativação, a data e horário de criação e a data e horaŕio de atualização.
A tabela de anúncios deve conter: a qual imóvel o anúncio pertence, nome da plataforma em que o anúncio foi publicado (ex: AirBnb) , a taxa da plataforma, a data e horário de criação e a data e horário de atualização.
A tabela de reservas deve conter: o código da reserva (gerado aleatoriamente), a qual anúncio a reserva pertence, data de check-in, data de check-out, preço total, campo de comentário, número de hóspedes, data e horário de criação e data e horário de atualização.
Datas e horários de criação e de atualização devem ser inseridos automaticamente no sistema, e não manualmente.

# Informações técnicas do projeto

### Clone ou donwload do projeto em:
https://github.com/ViniciusFSantos/projseazone.git

## Ferramentas utilizadas 
Python <br>
Django <br>
Django-Filter <br>
Django-Rest-Framework <br>
UUID <br>
SQLite3 (Banco de dados padrão do Django) <br>

## Sistema operacional utilizado no desenvolvimento:
Windows 10 Pro (para fins didáticos deste readme recomedo a utilização do mesmo sistema operacional usado no desenvolvimento)

## Instalação de dependências
Recomendo a criação e ativação de um ambiente virtual (venv) para instalação das dependências
que encontram-se em: projseazone/requirements.txt <br>

Comando para criação do venv > python -m venv venv <br>
Comando para ativar o venv > venv\scripts\activate <br>
Comando para instalação das dependências > pip install -r requirements.txt

## Migrations, fixtures e BD.
Antes de startar o servidor execute as migrations e importe as fixtures para o BD. <br>

 Comando para rodar migrations > pytohn manage.py makemigrations <br>
 Comando para executar as migrations > python manage.py migrate <br>
 Comando para executar as fixtures > python manage.py loaddata nome_da_api/fixtures/nome_do_arquivo.json <br>
 
 Cada API possui um diretório fixture basta subistituir os nomes no comando acima <br>
 api01imoveis > imoveis.json <br>
 api02anuncios > anuncios.json <br>
 api03reservas > reservas.json <br>
 
 Finalmente podemos rodar o servidor...
 Comando > python manage.py runserver <br>
 
 ## Funcionamento da aplicação CORE e APIs.
 A aplicação está dividia entre: <br>
 
 Diretório principal chamado khantoapp responsável pelas settings do projeto. <br>
 
 App Core:
 é responsável pelas models/migrations e direcionamento para as rotas principais das APIs <br>
 http://127.0.0.1:8000/imoveis <br>
 http://127.0.0.1:8000/anuncios <br>
 http://127.0.0.1:8000/reservas <br>
 
 3 APIs: <br>
 Sobre as consultas nas 3 APIs. <br>
 Temos 3 formas de faze-la: utilizando a rota principal que irá retornar a lista com todos os dados cadastrados, utilizando o botão de filtro onde podemos selecionar
 um critério para filtrar a listagem geral ou podemos através da url digitar o id do conjunto de dados que queremos exibir. <br>
 
 Sobre alteração e deleção nas APIs que permitem essas ações:
 Para alterar ou deletar é necessário passar o id do conjunto de dados que queremos pela url como por exemplo: <br>
 
 imoveis/3 <br>
 anuncios/1 <br>
 reservas/2be30338-8dd4-11ed-a1eb-0242ac120002 <br>
 Somente assim podemos alterar ou deletar um conjunto de dados. <br>
 
 Agora vejamos as ações que podemos executar em cada uma das APIs:<br>
 
 Na API Imoveis podemos: Consultar uma lista de imóveis, utilizar consulta personalizada pelo botão filtro, realizar consulta individual pelo id passado na url, criar
 um imóvel, alterar um imóvel e deletar um imóvel. <br>
 
 Na API Anuncios podemos: Consultar uma lista de anúncios, utilizar consulta personalizada pelo botão filtro, realizar consulta individual pelo id passado na url,
 criar um anúncio e alterar um anúncio. <br>
 
 Na API Reservas podemos: Consultar uma lista de reservas, utilizar consulta personalizada pelo botão filtro, realizar consulta individual pelo id passado na url,
 criar uma reserva e deletar uma reserva. <br>
  
 
 
