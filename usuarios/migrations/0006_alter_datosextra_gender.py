# Generated by Django 5.1.2 on 2024-10-31 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_datosextra_first_name_alter_datosextra_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosextra',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Mujer'), ('M', 'Hombre')], max_length=1, null=True),
        ),
    ]