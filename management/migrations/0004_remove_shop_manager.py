# Generated by Django 4.0.1 on 2022-02-16 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_qna_category_alter_address_member_alter_cart_memeber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='manager',
        ),
    ]