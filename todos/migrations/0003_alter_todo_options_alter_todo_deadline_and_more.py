# Generated by Django 5.0 on 2023-12-13 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_alter_todo_deadline_alter_todo_finished_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["deadline"]},
        ),
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(verbose_name="Data de Entrega"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Título"),
        ),
    ]
