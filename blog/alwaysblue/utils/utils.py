from alwaysblue.models import Blog, Author, Tag, Images
from BeautifulSoup import BeautifulSoup
import django_markdown

def findImageLinks():
    blog = Blog.objects.all()
    html = django_markdown.utils.markdown(value=blog.body)
    soup = BeautifulSoup(html)
    imgs = soup.findAll('img', {'src': True})
    for img in imgs:
        url = img['src']
