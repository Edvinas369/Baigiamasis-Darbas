from django.contrib import admin
from product.models import Category, Product, Images
from mptt.admin import DraggableMPTTAdmin


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = (
        "tree_actions",
        "indented_title",
        "related_products_count",
        "related_products_cumulative_count",)
    list_display_links = ("indented_title",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(
            qs, Product, "category", "products_cumulative_count", cumulative=True)

        qs = Category.objects.add_related_count(qs, Product, "category", "products_count", cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = ("Related products (for this specific category)")

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = "Related products (in tree)"

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(qs, Product, "category", "products_cumulative_count", cumulative=True)

        qs = Category.objects.add_related_count(qs, Product, "category", "products_count", cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count

    related_products_count.short_description = ("Related products (for this specific category)")

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count

    related_products_cumulative_count.short_description = "Related products (in tree)"


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "status"]
    list_filter = ["category"]
    readonly_fields = ("image_tag",)
    inlines = [ProductImageInline]


admin.site.register(Category, CategoryAdmin2)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
