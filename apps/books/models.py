import io
from io import StringIO

import pdfplumber
from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile
from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, FileField, ForeignKey, CASCADE, IntegerField, DateTimeField, ImageField


class Author(Model):
    name = CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Category(Model):
    name = CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Book(Model):
    title = CharField(max_length=250)
    price = IntegerField()
    image = ImageField(upload_to='book/images', blank=True, null=True)
    file = FileField(upload_to='book/files', validators=[FileExtensionValidator(['pdf'])])
    year = IntegerField()
    page_count = IntegerField(blank=True)
    added_date = DateTimeField(auto_now=True)

    """ relationships """
    author = ForeignKey('Author', CASCADE)
    user = ForeignKey(User, CASCADE)
    category = ForeignKey('Category', CASCADE)

    def save(self, *args, **kwargs):

        if self.file:
            self.page_count = self.get_num_pages()
        if not self.image:
            pass  # TODO: check image byte
            # from pdf2image import convert_from_bytes
            # self.file.seek(0)
            # images = convert_from_bytes(self.file.read(), first_page=1, fmt='jpeg', single_file=True)
            # name = self.file.name.split('.')[0] + '.jpeg'
            # self.image.save(name, ContentFile(StringIO(images[0].tobytes('UTF-8').decode('UTF-8')).read()))

        super().save(*args, **kwargs)

    def get_num_pages(self):
        with pdfplumber.open(self.file.file) as pdf:
            total_pages = len(pdf.pages)
            return total_pages

    class Meta:
        ordering = ('year',)
