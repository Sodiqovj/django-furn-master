# Generated by Django 4.0.4 on 2022-07-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furn', '0003_blog_category_product_subscribe_myuser_is_agent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrival',
            name='arrivals_text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arrival',
            name='arrvals_size',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
