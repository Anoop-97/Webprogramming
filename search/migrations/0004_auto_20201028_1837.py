# Generated by Django 3.1.2 on 2020-10-28 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20201028_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='figure_details',
            name='aspect',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='description',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='figid',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='is_caption',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='is_multiple',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='object',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='origreftext',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='figure_details',
            name='subfig',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='figure_details',
            name='patentID',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='figure_details',
            name='pid',
            field=models.CharField(default=None, max_length=50),
        ),
    ]