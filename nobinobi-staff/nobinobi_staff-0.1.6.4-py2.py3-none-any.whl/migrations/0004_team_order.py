#  Copyright (C) 2020 <Florian Alu - Prolibre - https://prolibre.com
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# Generated by Django 2.0.9 on 2018-10-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nobinobi_staff', '0003_auto_20181022_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='order',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='Order'),
        ),
    ]
