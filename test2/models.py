from django.db import models
class Category(models.Model):
#Category
    name = models.CharField("Категория", max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Actor(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveIntegerField('Возраст', default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors/")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Актеры и режисеры"
        verbose_name_plural = "Актеры и режисеры"

class Genre(models.Model):
    name = models.CharField("Иия", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    poster = models.ImageField('Постер', upload_to="movies/")
    description = models.TextField('Opisanie')
    year = models.PositiveSmallIntegerField('date reales', default=2022)
    country = models.CharField('Страна', max_length=30)
    actors = models.ManyToManyField(Actor, verbose_name="актеры",related_name="film_director")
    genres = models.ManyToManyField(Actor, verbose_name="жанры")
    fees_in_kg = models.PositiveIntegerField(
        "Сборы в Кыргызстане",default=0,help_text="указывать сумму в доллпрах"
    )
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=130, unique=True
                           )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "film"
        verbose_name_plural = "film"
