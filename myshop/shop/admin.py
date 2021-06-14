from django.contrib import admin

# Register your models here.


from .models import Category, Product, Alloy, InsertIn, Brend, Comment

class AlloyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Alloy, AlloyAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class InsertInAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(InsertIn, InsertInAdmin)

class BrendAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Brend, BrendAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'timestamp']
    
admin.site.register(Comment, CommentAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category', 'alloy']
    list_editable = ['price', 'stock', 'available']
    readonly_fields=('id',)
    search_fields = ('id', 'name')

    fieldsets = (
    	(None, {
    	'fields' : (('name', 'slug', 'id'), 'category' , 'price', ('brend', 'alloy','insertin'), 'image','size_ring' ,('size_x', 'size_y', 'size_z'), 'weight', 'description', 'stock', 'available')
    	}),
    )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

