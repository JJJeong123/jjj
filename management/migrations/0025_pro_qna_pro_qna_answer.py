# Generated by Django 4.0.1 on 2022-05-07 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0024_alter_qna_answer_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro_qna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='삭제시간')),
                ('DeleteFlag', models.CharField(blank=True, db_column='DeleteFlag', default='0', max_length=10, null=True)),
                ('title', models.CharField(blank=True, db_column='title', max_length=50, null=True)),
                ('content', models.CharField(blank=True, db_column='content', max_length=50, null=True)),
                ('password', models.CharField(blank=True, db_column='password', max_length=50, null=True)),
                ('answer_flag', models.CharField(blank=True, db_column='answer_flag', default='0', max_length=10, null=True)),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.member', verbose_name='member')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.product', verbose_name='product')),
            ],
            options={
                'db_table': 'pro_qna',
            },
        ),
        migrations.CreateModel(
            name='pro_qna_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
                ('deleted_at', models.DateTimeField(null=True, verbose_name='삭제시간')),
                ('DeleteFlag', models.CharField(blank=True, db_column='DeleteFlag', default='0', max_length=10, null=True)),
                ('content', models.TextField(blank=True, db_column='content', null=True)),
                ('qna', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='management.pro_qna', verbose_name='pro_qna')),
            ],
            options={
                'db_table': 'pro_qna_answer',
            },
        ),
    ]
