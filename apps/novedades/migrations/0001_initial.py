# Generated by Django 3.2.8 on 2021-12-03 06:44

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInasistencia',
            fields=[
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha creacion')),
                ('fecha_modificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha modificacion')),
                ('fecha_eliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('idInasistencia', models.BigIntegerField(blank=True, db_index=True)),
                ('fechaReporte', models.DateTimeField(blank=True, editable=False)),
                ('descripcionInasistencia', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Inasistencia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalNovedad',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('fichaAspirante', models.IntegerField(blank=True, default=0)),
                ('estadoNovedad', models.CharField(max_length=40)),
                ('comentario', models.CharField(blank=True, max_length=100)),
                ('fechaInicio', models.CharField(blank=True, max_length=100)),
                ('causa', models.CharField(blank=True, max_length=100)),
                ('duracionA', models.IntegerField(blank=True, default=0)),
                ('acta', models.TextField(blank=True, max_length=100)),
                ('fechaSolicitud', models.CharField(max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Novedad',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTipoNovedad',
            fields=[
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(blank=True, editable=False, verbose_name='Fecha creacion')),
                ('fecha_modificacion', models.DateField(blank=True, editable=False, verbose_name='Fecha modificacion')),
                ('fecha_eliminacion', models.DateField(blank=True, editable=False, verbose_name='Fecha eliminacion')),
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('tipoNovedad', models.CharField(db_index=True, max_length=30)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Tipo Novedad',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Inasistencia',
            fields=[
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('idInasistencia', models.BigAutoField(primary_key=True, serialize=False)),
                ('fechaReporte', models.DateTimeField(auto_now_add=True)),
                ('descripcionInasistencia', models.TextField()),
            ],
            options={
                'verbose_name': 'Inasistencia',
                'verbose_name_plural': 'Inasistencias',
            },
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichaAspirante', models.IntegerField(blank=True, default=0)),
                ('estadoNovedad', models.CharField(max_length=40)),
                ('comentario', models.CharField(blank=True, max_length=100)),
                ('fechaInicio', models.CharField(blank=True, max_length=100)),
                ('causa', models.CharField(blank=True, max_length=100)),
                ('duracionA', models.IntegerField(blank=True, default=0)),
                ('acta', models.FileField(blank=True, upload_to='solicitudes/')),
                ('fechaSolicitud', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Novedad',
                'verbose_name_plural': 'Novedades',
            },
        ),
        migrations.CreateModel(
            name='TipoNovedad',
            fields=[
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha eliminacion')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipoNovedad', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo Novedad',
                'verbose_name_plural': 'Tipos de Novedad',
            },
        ),
        migrations.CreateModel(
            name='DetalleNovedad',
            fields=[
                ('novedad_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='novedades.novedad')),
                ('DescripcionNovedad', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Detalle de novedad',
                'verbose_name_plural': 'Detalles de novedades',
            },
            bases=('novedades.novedad',),
        ),
    ]
