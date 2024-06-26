# Generated by Django 4.2.11 on 2024-04-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('certification_pic', models.ImageField(blank=True, null=True, upload_to='certification_pic/')),
                ('certificate_icon_pic', models.ImageField(blank=True, null=True, upload_to='certificate_icon_pic/')),
                ('provider', models.CharField(max_length=200)),
                ('date_completed', models.DateField()),
                ('certification_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('degree_city', models.CharField(max_length=200)),
                ('university_logo', models.ImageField(blank=True, null=True, upload_to='university_logo/')),
                ('degree_pic', models.ImageField(blank=True, null=True, upload_to='degree_pic/')),
                ('institution', models.CharField(max_length=200)),
                ('completion_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('name_preferred', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_num', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('address', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_link', models.URLField(blank=True, null=True)),
                ('project_topic', models.CharField(choices=[('Machine Learning', 'Machine Learning'), ('Data Science', 'Data Science'), ('Data Analytics', 'Data Analytics'), ('Software Engineer', 'Software Engineer'), ('Others', 'Others')], default='active', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('project_pic', models.ImageField(blank=True, null=True, upload_to='project_pics/')),
                ('tech_stack', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('skill_logo', models.ImageField(blank=True, null=True, upload_to='skill_logo/')),
                ('Percentage', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('responsibilities', models.TextField()),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='company_logo/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
            ],
        ),
    ]
