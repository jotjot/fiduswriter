# Generated by Django 2.2.3 on 2019-08-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0013_auto_20190808_1126'),
        ('style', '0006_auto_20190809_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documenttemplate',
            name='document_styles',
        ),
        migrations.RemoveField(
            model_name='documenttemplate',
            name='export_templates',
        ),
        migrations.DeleteModel(
            name='ExportTemplate',
        ),
    ]
