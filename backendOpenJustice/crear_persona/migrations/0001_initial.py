# Generated by Django 5.0.3 on 2024-03-07 18:45

import crear_persona.models
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('pais', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crear_persona.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('numeroDocumento', models.CharField(max_length=20, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^\\d{1,20}$')])),
                ('tipoDocumento', models.CharField(max_length=30)),
                ('primerApellido', models.CharField(max_length=30)),
                ('segundoApellido', models.CharField(max_length=30)),
                ('prenombres', models.CharField(max_length=80)),
                ('fechaNacimiento', models.DateField()),
                ('estadoCivil', models.CharField(max_length=1, validators=[crear_persona.models.validate_estado_civil])),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crear_persona.nacionalidad')),
                ('paisOrigen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crear_persona.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cargo', models.CharField(max_length=30)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True, validators=[django.core.validators.RegexValidator('^\\d{9}$')])),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('datos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crear_persona.persona', unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
