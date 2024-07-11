# Generated by Django 5.0.6 on 2024-06-25 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_userprofile_profile_picture'),
        ('events', '0007_remove_event_bookmark_remove_event_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_bookmarks', to='accounts.userprofile')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_bookmarks', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Comment Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_comments', to='accounts.userprofile')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_comments', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_likes', to='accounts.userprofile')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_likes', to='events.event')),
            ],
        ),
    ]