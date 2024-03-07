from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify



# Create your models here.
class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='upload/img/')
    
    class Meta:
        verbose_name_plural ='Thể loại tin tức'
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    post_catalogue = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = HTMLField()
    content = RichTextUploadingField(null = True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.CharField(max_length=255, unique=True)
    meta_title = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    meta_description = models.TextField()
    
    class Meta:
        verbose_name_plural ='Tin tức'
    
    def save(self, *args, **kwargs):
        # Tạo URL từ trường 'name' và kiểm tra tính duy nhất
        self.url = slugify(self.name)
        if Post.objects.filter(url=self.url).exclude(id=self.id).exists():
            base_url = self.url
            counter = 1
            while Post.objects.filter(url=self.url).exclude(id=self.id).exists():
                self.url = f"{base_url}-{counter}"
                counter += 1

        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(blank=True, null=True) # lưu giữa ip của người bình luận

    class Meta:
        verbose_name_plural ='Bình luận'
    
    def __str__(self):
        return self.comment
    