from django.shortcuts import render, get_object_or_404, redirect
from .models import Task 
# Create your views here.
# my_app/views.py


# صفحة البداية (Home)
def home(request):
    return render(request, 'my_app/home.html')

# عرض جميع المهام
def index(request):
    tasks = Task.objects.all()
    return render(request, 'my_app/index.html', {'tasks': tasks})

# عرض تفاصيل المهمة
def detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'my_app/detail.html', {'task': task})

# إنشاء مهمة جديدة
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task_list')  # العودة إلى صفحة قائمة المهام بعد الإنشاء
    return render(request, 'my_app/create.html')

# تعديل مهمة موجودة
def edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task_list')  # العودة إلى صفحة قائمة المهام بعد التعديل
    return render(request, 'my_app/edit.html', {'task': task})

# حذف مهمة
def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')  # العودة إلى صفحة قائمة المهام بعد الحذف
