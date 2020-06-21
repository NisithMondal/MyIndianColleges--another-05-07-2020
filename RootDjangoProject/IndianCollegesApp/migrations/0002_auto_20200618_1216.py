# Generated by Django 3.0.2 on 2020-06-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndianCollegesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcolleges',
            name='affilicated_by',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='city_name',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='college_fees_per_semester',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='college_name',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='college_rank',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='college_type',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='college_website_link',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='course_duration',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='course_type',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='established_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='exams_for_admission',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='state_name',
            field=models.CharField(max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='allcolleges',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]