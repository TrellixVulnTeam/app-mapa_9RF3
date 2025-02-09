# Generated by Django 4.0 on 2022-05-12 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_emp', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_emp', models.CharField(max_length=25)),
                ('apellido_emp', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_ciudad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_comuna', models.CharField(max_length=50)),
                ('ciudad_id_ciudad', models.ForeignKey(db_column='ciudad_id_ciudad', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Duenno',
            fields=[
                ('rut_duenno', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('pnombre', models.CharField(max_length=30)),
                ('snombre', models.CharField(blank=True, max_length=30, null=True)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('telefono', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_marca', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_modelo', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_modelo', models.CharField(max_length=50)),
                ('annio', models.IntegerField()),
                ('marca_id_marca', models.ForeignKey(db_column='marca_id_marca', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.marca')),
            ],
            options={
                'unique_together': {('id_modelo', 'marca_id_marca')},
            },
        ),

        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('color', models.CharField(max_length=25)),
                ('num_ruedas', models.BooleanField()),
                ('duenno', models.ForeignKey(db_column='dueño_rut_dueño', on_delete=django.db.models.deletion.DO_NOTHING, related_name='rut_dueño', to='Parking.duenno')),
                ('marca', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.marca')),
                ('modelo', models.ForeignKey(db_column='modelo_id_modelo', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.modelo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut_user', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nom_user', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('pnombre', models.CharField(max_length=30)),
                ('snombre', models.CharField(blank=True, max_length=30, null=True)),
                ('apaterno', models.CharField(max_length=30)),
                ('amaterno', models.CharField(max_length=30)),
                ('gmail', models.CharField(max_length=45)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('comuna_id_comuna', models.ForeignKey(db_column='comuna_id_comuna', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.comuna')),
                ('vehiculo_patente', models.ForeignKey(db_column='vehiculo_patente', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.vehiculo')),
            ],
            options={
                'unique_together': {('rut_user', 'vehiculo_patente')},
            },
        ),


    ]
