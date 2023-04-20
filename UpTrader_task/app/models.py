from django.db import models
from django.urls import reverse
from django.http import Http404


class MenuItem(models.Model):
    name = models.CharField(max_length=50, blank=True, null=False)  # поле модели MenuItem, которое представляет название элемента меню
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)  # поле модели, которое представляет родительский элемент меню
    explicit_url = models.CharField(max_length=100, blank=True, null=True, unique=True)  # поле модели, которое представляет явный URL-адрес элемента меню

    # переопределенный метод, который возвращает строковое представление объекта модели MenuItem
    def __str__(self):
        return self.name

    # метод, который возвращает дочерние элементы данного элемента меню
    def children(self):
        return self.menuitem_set.all()

    # метод, который возвращает список идентификаторов всех родительских элементов данного элемента меню
    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
