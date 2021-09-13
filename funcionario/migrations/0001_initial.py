# Generated by Django 3.2.7 on 2021-09-13 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField(verbose_name='Matricula')),
                ('nome', models.CharField(help_text='Nome do funcionário', max_length=100)),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
        ),
    ]
