# Generated by Django 3.0.8 on 2020-08-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railway', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routerank',
            name='int_stop',
        ),
        migrations.RemoveField(
            model_name='routerank',
            name='prob',
        ),
        migrations.RemoveField(
            model_name='routerank',
            name='train_no_intStop_to_dest',
        ),
        migrations.RemoveField(
            model_name='routerank',
            name='train_no_src_to_intStop',
        ),
        migrations.AddField(
            model_name='routerank',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='routerank',
            name='train_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
