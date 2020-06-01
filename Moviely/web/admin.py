from django.contrib import admin
from .models import Movie,Myrating

class MovieAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('title', 'genre', 'movie_logo')
    def download_csv(self, request, queryset):
        import csv
        f = open('some.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['title', 'genre', 'movie_logo'])
        
        # print(queryset)
        for s in queryset:
            # print(s)
            writer.writerow([s.title, s.genre, str(s.movie_logo)])
    download_csv.short_description = "Download CSV file for selected Movies."
class MyratingAdmin(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('user', 'movie', 'rating')
    def download_csv(self, request, queryset):
        import csv
        f = open('some2.csv', 'w')
        writer = csv.writer(f)
        writer.writerow(['user', 'movie', 'rating'])
        
        # print(queryset)
        for s in queryset:
            # print(s)
            writer.writerow([s.user, s.movie, s.rating])
    download_csv.short_description = "Download CSV file for selected Movies."
admin.site.register(Movie, MovieAdmin)

admin.site.register(Myrating,MyratingAdmin)
# Register your models here.
