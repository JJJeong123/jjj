# Generated by Django 4.0.1 on 2022-05-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0023_alter_qna_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna_answer',
            name='content',
            field=models.TextField(blank=True, db_column='content', null=True),
        ),
    ]