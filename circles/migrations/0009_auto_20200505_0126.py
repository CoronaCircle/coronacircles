# Generated by Django 3.0.5 on 2020-05-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0008_auto_20200505_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='language_code',
            field=models.CharField(choices=[('de', 'German'), ('en', 'English')], default='en', max_length=2, verbose_name='Language'),
        ),
    ]
