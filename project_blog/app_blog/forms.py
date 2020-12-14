from django.forms import ModelForm

from .models import SamplePostBlog 
from .models import DestaquePostBlog

class SamplePostBlogForm(ModelForm):
    class Meta:
        model = SamplePostBlog
        fields = ['title','descricao']

class DestaquePostBlogForm(ModelForm):
    class Meta:
        model = DestaquePostBlog
        fields = ['title','descricao','imagem']