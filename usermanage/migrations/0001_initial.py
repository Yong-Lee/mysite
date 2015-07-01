# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userip', models.IPAddressField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('userauth', models.CharField(max_length=32, verbose_name='\u6743\u9650', choices=[(b'0', b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98'), (b'1', b'\xe6\x99\xae\xe9\x80\x9a\xe7\x94\xa8\xe6\x88\xb7')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
