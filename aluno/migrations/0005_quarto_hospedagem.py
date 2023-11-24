# Generated by Django 4.2.2 on 2023-11-23 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.IntegerField()),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField()),
                ('data_saida', models.DateField()),
                ('valor', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.cliente')),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aluno.quarto')),
            ],
        ),
    ]
