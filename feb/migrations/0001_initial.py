# Generated by Django 4.1.2 on 2022-10-06 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.CharField(max_length=9)),
                ('Nama', models.TextField()),
                ('Tanggallahir', models.TextField()),
                ('Photo', models.TextField()),
                ('Email', models.TextField()),
                ('Fakultas', models.TextField()),
                ('Prodi', models.TextField()),
                ('Alamatrumah', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIM', models.CharField(max_length=9)),
                ('Nama', models.TextField()),
                ('Tanggallahir', models.TextField()),
                ('Photo', models.TextField()),
                ('Email', models.TextField()),
                ('Fakultas', models.TextField()),
                ('Prodi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tendik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.CharField(max_length=9)),
                ('Nama', models.TextField()),
                ('Tanggallahir', models.TextField()),
                ('Photo', models.TextField()),
                ('Email', models.TextField()),
                ('Unit', models.TextField()),
                ('Alamatrumah', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='faperta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=50)),
                ('Dosen_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.dosen')),
                ('Mahasiswa_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.mahasiswa')),
                ('Tendik_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.tendik')),
            ],
        ),
    ]
