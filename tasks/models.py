from django.contrib.auth import get_user_model
from django.db import models

from tasks.constace import STATUS_CHOICES

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Наименование категории")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата обновления")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Priority(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Приоритетность")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата обновления")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")

    class Meta:
        verbose_name = "Приоритет"
        verbose_name_plural = "Приоритеты"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Постановщик",
        related_name="tasks",
    )
    title = models.CharField(max_length=100, unique=True, verbose_name="Наименование задачи")
    description = models.TextField(verbose_name="Описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo", verbose_name="Статус")
    completed = models.BooleanField(default=False, verbose_name="Завершено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата завершения")
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата обновления")
    deleted_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата удаления")
    deleted = models.BooleanField(default=False, verbose_name="Удалено")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        related_name="tasks"
    )
    priority = models.ForeignKey(
        Priority,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Приоритет",
        related_name="tasks"
    )

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
