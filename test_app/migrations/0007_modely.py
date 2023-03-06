# Generated by Django 4.1.7 on 2023-03-04 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_alter_testmodel_options_modelx'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='test_content_y', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelY',
                'ordering': ('-created_at',),
            },
        ),
    ]
