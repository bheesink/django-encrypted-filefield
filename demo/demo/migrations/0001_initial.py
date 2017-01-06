# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django_encrypted_filefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('attachment', django_encrypted_filefield.fields.EncryptedFileField(upload_to='attachments')),
                ('image', django_encrypted_filefield.fields.EncryptedImageField(height_field='image_height', upload_to='images', width_field='image_width')),
                ('image_width', models.PositiveIntegerField()),
                ('image_height', models.PositiveIntegerField()),
            ],
        ),
    ]