from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    first_name = models.CharField("Имя", max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    last_login = None
    groups = None
    # surname = models.CharField("Фамилия", max_length=100)
    # name = models.CharField("Имя", max_length=100)
    fatherland = models.CharField("Отчество", max_length=100, blank=True)
    profession = models.CharField("Профессия", max_length=100)
    date_of_Birth = models.DateField("Дата Рождения", default=timezone.now)
    phone = models.CharField("Номер Телефона", max_length=50, unique=True)
    address = models.CharField("Адрес", max_length=100)
    city = models.CharField("Город", max_length=100)
    country = models.CharField("Страна", max_length=100)
    place_of_work = models.CharField("Место Работы", max_length=100)
    job = models.CharField("Должность", max_length=100)


class BasePost(models.Model):
    title = models.CharField("Название", max_length=100)
    text = models.TextField("Текст", null=True)
    paid = models.BooleanField("Платный", default=False)
    main_image = models.ImageField("Основное фото", upload_to="post/img/")
    date = models.DateField("Дата Публикации", default=timezone.now)
    youtube_url = models.CharField("Ютуб Ссылка", blank=True, max_length=150, null=True)
    draft = models.BooleanField("Черновик", default=False)

    @property
    def main_image_preview(self):
        return mark_safe(f'<img src="{self.main_image.url}" width="400" />')

    class Meta:
        abstract = True


class Post(BasePost):
    category = models.CharField("Категория", max_length=50)
    tags = models.CharField("Теги", max_length=50)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Event(BasePost):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятия"


class News(BasePost):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Post_Images(models.Model):
    image = models.ImageField("фото", upload_to="post/img")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class Event_Images(models.Model):
    image = models.ImageField("фото", upload_to="event/img")
    post = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"


class News_Images(models.Model):
    image = models.ImageField("фото", upload_to="news/img")
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"