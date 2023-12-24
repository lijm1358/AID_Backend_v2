# Generated by Django 4.2.8 on 2023-12-24 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apply",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=40)),
                ("email", models.TextField(unique=True)),
                ("student_id", models.TextField(unique=True)),
                ("phone_number", models.CharField(max_length=11)),
                ("motive", models.CharField(max_length=500)),
                ("github_link", models.TextField()),
                ("blog_link", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=45)),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nickname", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=45, unique=True)),
                ("password", models.CharField(max_length=45)),
                ("is_admin", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("tag", models.CharField(max_length=45)),
                ("questions", models.ManyToManyField(to="testapp.question")),
            ],
        ),
        migrations.CreateModel(
            name="Study",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("study_name", models.CharField(max_length=50)),
                ("study_description", models.CharField(max_length=300)),
                ("study_link", models.CharField(max_length=500, null=True)),
                ("status", models.IntegerField()),
                ("img_url", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "leader_id",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="leader",
                        to="testapp.user",
                    ),
                ),
                ("users", models.ManyToManyField(related_name="participants", to="testapp.user")),
            ],
        ),
        migrations.CreateModel(
            name="Reply",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("comment_id", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="testapp.comment")),
                ("writer_id", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="testapp.user")),
            ],
        ),
        migrations.AddField(
            model_name="question",
            name="writer_id",
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="testapp.user"),
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("project_name", models.CharField(max_length=45)),
                ("project_description", models.TextField()),
                ("project_link", models.CharField(max_length=500, null=True)),
                ("status", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("users", models.ManyToManyField(to="testapp.user")),
            ],
        ),
        migrations.CreateModel(
            name="Competition",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("competition_name", models.CharField(max_length=45)),
                ("competition_description", models.TextField()),
                ("competition_link", models.CharField(max_length=500, null=True)),
                ("status", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("users", models.ManyToManyField(to="testapp.user")),
            ],
        ),
        migrations.AddField(
            model_name="comment",
            name="question_id",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="testapp.question"),
        ),
        migrations.AddField(
            model_name="comment",
            name="writer_id",
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to="testapp.user"),
        ),
    ]
