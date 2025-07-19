"""
Admin configuration for listings app.
"""
from django.contrib import admin
from .models import Listing, ListingImage

class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1
    fields = ['image', 'alt_text', 'is_primary']

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'property_type', 'price_per_night', 'is_available', 'host', 'created_at']
    list_filter = ['property_type', 'is_available', 'created_at', 'location']
    search_fields = ['title', 'description', 'location', 'host__username']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [ListingImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'property_type', 'host')
        }),
        ('Location & Pricing', {
            'fields': ('location', 'latitude', 'longitude', 'price_per_night')
        }),
        ('Property Details', {
            'fields': ('max_guests', 'bedrooms', 'bathrooms', 'amenities')
        }),
        ('Availability', {
            'fields': ('is_available',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ['listing', 'alt_text', 'is_primary', 'created_at']
    list_filter = ['is_primary', 'created_at']
    search_fields = ['listing__title', 'alt_text']
