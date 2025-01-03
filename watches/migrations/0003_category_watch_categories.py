# Generated by Django 4.2 on 2024-11-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watches', '0002_watch_user_alter_watch_discount_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='watch',
            name='categories',
            field=models.ManyToManyField(to='watches.category'),
        ),
    ]
