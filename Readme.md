Nesta pasta estão os estudos direcionados de:

GIT
Javascript
C#
Python
Django
Flask

Git:
Comandos:

Criação de repositorio GIT
-----------------------------------------------------------------------------------------

git init/ Inicia um repositório vazio

git add "Nome do arquivo"/ Envia os arquvios para um modo de stage(Preparado para commit)
    ou
git add . / Envia todos os arquivos disponiveis para o repositório


git status/ Mostra todas as mudanças a serem "Commitadas"

git commit - m "Titulo do commit"/ Commita as informações para o repositório 

GIT STATUS/ mostrará que não há mais nada a ser inserido

git branch -M "main"/ renomeia a branch principal para o nome definido

git remote add origin https://github.com/RhyanLucca/EstudosGit /Adiciona uma conexão remota do repositório com o github pelo link

git push -u origin main/ Primeira vez que você cria o repositorio

git push origin main / pós o primeiro uso não tem mais necessidade de usar o "-U"

---------------------------------------------------------------------------------------
Criação de uma nova branch

git checkout -b "novo-botão" / Cria uma branch nova para alteração

git add .

git commit - m "Titulo do commit"

git push origin "Nome da branch" EX:Novo botao 

AQUI TEMOS UMA ALTERAÇÃO PARA TESTE DE VERSIONAMENTO