# Generated by Django 3.1.4 on 2021-01-30 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0002_auto_20201220_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='documentation',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='documentation.category'),
        ),
    ]
