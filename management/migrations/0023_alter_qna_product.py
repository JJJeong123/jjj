# Generated by Django 4.0.1 on 2022-05-04 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0022_qna_qna_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.product', verbose_name='product'),
        ),
    ]
