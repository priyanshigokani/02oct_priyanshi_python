# Generated by Django 5.1.6 on 2025-03-04 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_alter_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('Romance', 'Romance'), ('Action_Adventure', 'Action & Adventure'), ('Mystery_Thriller', 'Mystery & Thriller'), ('Biographies_History', 'Biographies & History'), ('Children', 'Children'), ('Young_Adult', 'Young Adult'), ('Fantasy', 'Fantasy'), ('Historical_Fiction', 'Historical Fiction'), ('Horror', 'Horror'), ('Literary_Fiction', 'Literary Fiction'), ('Non_fiction', 'Non-fiction'), ('Science_Fiction', 'Science Fiction')], max_length=100),
        ),
    ]
