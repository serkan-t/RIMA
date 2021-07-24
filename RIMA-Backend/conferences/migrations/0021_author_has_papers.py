# Generated by Django 2.2.3 on 2021-07-24 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0020_remove_author_papers_within_conference'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author_has_Papers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Author')),
                ('conference_event_name_abbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference_Event')),
                ('conference_name_abbr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference')),
                ('paper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference_Event_Paper')),
            ],
            options={
                'unique_together': {('conference_event_name_abbr', 'author_id', 'paper_id')},
            },
        ),
    ]
