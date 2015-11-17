from django.contrib import admin
from .models import Question, Choice
# Register your models here.
# let the model Question in the admin site


class ChoiceInline(admin.TabularInline):
    # link the inline to the model choice
    model = Choice
    # add two extra block
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}), ('Date information', {
        'fields': ['pub_date'], 'classes':['collapse']}), ]
    # add foregin key in question
    inlines = [ChoiceInline]
    # add more information in the title
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # ..add filter in the admin site for anydate? today? past 7 days? etc..
    list_filter = ['pub_date']
    # ..add search_field in the admin site
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
