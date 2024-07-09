# Generated by Django 4.1.2 on 2023-08-10 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_rename_created_support_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='support',
            old_name='created_at',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='support',
            name='Situation',
            field=models.CharField(choices=[('pending', 'pending'), ('Done', 'Done')], default='Pending', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='support',
            name='option',
            field=models.CharField(choices=[('Update resume', 'Update resume'), ('Others', 'Others'), ('l lost my account', 'l lost my account'), ('My password does not work', 'My password does not work')], max_length=50),
        ),
    ]
