# Generated by Django 3.2 on 2021-12-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_order_customernumber_order_items_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orderfood',
            name='order',
        ),
        migrations.AddField(
            model_name='food',
            name='slug',
            field=models.SlugField(default='food'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='foods',
            field=models.ManyToManyField(to='store.OrderFood'),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderfood',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderfood',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
