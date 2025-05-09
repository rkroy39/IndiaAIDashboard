# Generated by Django 5.2 on 2025-04-30 05:50

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indiaAI_Dashboard', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HistoricalLoginAuditTrail2',
            new_name='HistoricalLoginAuditTrail',
        ),
        migrations.RenameModel(
            old_name='LoginAuditTrail2',
            new_name='LoginAuditTrail',
        ),
        migrations.AlterModelOptions(
            name='historicalloginaudittrail',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical login audit trail', 'verbose_name_plural': 'historical login audit trails'},
        ),
        migrations.CreateModel(
            name='NavigationBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=255, unique=True)),
                ('page_url', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
