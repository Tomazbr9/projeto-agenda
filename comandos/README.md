python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact


migrando a base de dados do django

python manage.py makemigrations
python manage.py migrate

criando e modificando a senha de um usuario django

python manage.py createsuperuser
python manage.py changepassword nomeusuario

Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT