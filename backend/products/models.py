from django.db import models

# Create your models here.
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    prep_time = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')