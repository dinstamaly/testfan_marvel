from django.contrib import admin
from .models import (
    Subject,
    Quiz,
    Question,
    Answer,
    Student,
    TakenQuiz,
    User

)


admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)
admin.site.register(User)
