# Generated by Django 5.2 on 2025-04-04 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0004_usuario_tarefas_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tarefas',
            new_name='Tarefa',
        ),
    ]
