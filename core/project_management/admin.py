from django.contrib import admin
from .models import Deadline,Priority,Project,Task,Status,HistoryLog
admin.site.register(Deadline)
admin.site.register(Priority)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(HistoryLog)
