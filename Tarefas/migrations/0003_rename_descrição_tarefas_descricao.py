# Generated by Django 3.2.4 on 2021-07-04 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefas', '0002_rename_descricao_tarefas_descrição'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefas',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
