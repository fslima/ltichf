Lista telefônica do ICHF
+++++++++++++++++++++++

Tecnologia da Informação Instituto de Ciências Humanas / Universidade Federal Fluminense
_______________________

Instalação o Projeto
=====================

#Instalação do Django 1.3.1
apt-get install python-dev libpq-dev python-setuptools build-essential python-pip
easy_install pip
pip install django==1.3.1

#Instalação do POSTGRE 8.4
apt-get install postgresql-8.4
apt-get install python-pgsql

#Configurando o Sistema do Ditex
cd "local" 				#Acessar local para onde foi realizado download do projeto
mkdir /opt/github	
mkdir /opt/github/ltichf
chmod 777 /opt/github/ltichf		
cp -a . /opt/github/ltichf
sudo -u "usuario_banco" createdb lista 	#No arquivo settings.py deve ser mapeado o nome e senha do usuário do banco
python /opt/github/ltichfmanage.py syncdb

Durante a execução deverá ser criado um super usuário para o Django.

Será perguntado se deseja criar o super usuário, deve-se digitar "yes", digitar o usuário, email e senha.


Rodar o Projeto
================
Após a conclusão da instalação executar o comando: python manage.py runserver no diretório /opt/github/ltichf

A página inicial do sistema é http://localhost:8000

A parte de administração deve ser acessada com a conta e senha do super usuario do Django.

Esse é apenas um servidor de teste, para colocar em produção deve ser configurado um servidor web como apache
