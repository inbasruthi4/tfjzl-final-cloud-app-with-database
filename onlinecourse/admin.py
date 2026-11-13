
from django.contrib import admin

# Import seven model classes
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission
)


# Lesson Inline
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Choice Inline
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


# Question Inline
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('content', 'course', 'grade')
    list_filter = ['course']
    search_fields = ['content']


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
