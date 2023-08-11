from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)

#
class UsuarioManager(BaseUserManager):

    def create_user(self, email, password):
        usuario = self.model(
            email=self.normalize_email(email),
            password=password
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        usuario.set_password(password) 

        usuario.save()

        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password= password
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password) 

        usuario.save()

        return usuario


#Alteração de padrão de usuarios

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name= "E-mail do usuario",
        max_length=194,
        unique=True
    )

    is_active = models.BooleanField( #define se o usuario está ativo
        verbose_name= "Usuário está ativo",
        default=True
    )

    is_staff = models.BooleanField( #define se o usuario é da equipe de desenvolvimento
        verbose_name= "Usuário é da equipe de desenvolvimento?",
        default=False
    )

    is_superuser = models.BooleanField( #define se o usuario é um superusuario
        verbose_name="Usuário é um super-usuário",
        default=False
    )

    #Define a credencial principal para o acesso ao ashboard
    USERNAME_FIELD = "email"

    objects = UsuarioManager()

    #Metadados
    class Meta:
        verbose_name = "Usuário", #Serve para dar um apelido para o modelo
        verbose_name_plural = "Usuários",
        db_table= "usuario" #Nome da tabela no banco


    #Obrigatorio pois sempre é chamado sempre que transfrmamos o objeto (Instancia da clase usuario) em uma string para fins de exibição
    def __str__(self):
        return self.email
    
