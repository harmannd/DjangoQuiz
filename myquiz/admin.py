from django.contrib import admin
from django.utils.html import format_html

from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)


class QuestionInline(admin.TabularInline):
    model = Question

    def question_link(self, instance):
        url = "../../../question/" + str(instance.id) + "/change/"
        return format_html(u'<a href="{}">Edit</a>', url)
    readonly_fields = ('question_link',)


class QuizAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['quiz_name']}),
    ]
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)

