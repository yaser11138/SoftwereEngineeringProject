# Generated by Django 4.2.7 on 2023-11-22 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0003_alter_discussion_options_discussion_is_answered"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ticket",
            options={"ordering": ("-sent_date",)},
        ),
    ]
