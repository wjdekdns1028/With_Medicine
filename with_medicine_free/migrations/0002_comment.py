# Generated by Django 4.2.1 on 2023-08-05 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_free', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_text', models.CharField(max_length=30)),
                ('free_board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_comment', to='with_medicine_free.free_board')),
            ],
        ),
    ]
