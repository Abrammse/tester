# Generated by Django 4.0.5 on 2024-06-05 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my', '0002_events_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcases',
            old_name='Action',
            new_name='bady',
        ),
        migrations.RemoveField(
            model_name='testcases',
            name='Expected_Result',
        ),
        migrations.RemoveField(
            model_name='testcases',
            name='preconditions',
        ),
        migrations.AddField(
            model_name='testcases',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='my.staffs'),
        ),
    ]
