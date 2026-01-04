
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# HOME / READ
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

# CREATE
def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'form.html', {'form': form})

# UPDATE
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'form.html', {'form': form})

# DELETE
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('index')
    return render(request, 'delete.html', {'student': student})
