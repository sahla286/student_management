from django.shortcuts import render,redirect
from django.views import View
from .forms import StudentModelForm,LoginForm,RegistrationForm
from .models import Student
from django.contrib.auth import authenticate
from django.contrib import messages

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        formdata=LoginForm(data=request.POST)
        if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                return redirect('landing')
            else:
                messages.error(request,'Login Failed!!')
                return redirect('login')
        return render(request,'login.html',{'form':formdata})
        
class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
    def post(self,request):
        formdata=RegistrationForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,'Registration Successfully')
            return redirect('login')
        messages.error(request,'Registration Failed!!')
        return render(request,'registration.html',{'form':formdata})

class LandingView(View):
    def get(self,request):
        return render(request,'landing.html')

class DashboardView(View):
    def get(self,request):
        data=Student.objects.all()
        return render(request,'dashboard.html',{'data':data})
    
class AddView(View):
    def get(self,request):
        form=StudentModelForm()
        return render(request,'addstudent.html',{'form':form})
    
    def post(self, request):
        form_data = StudentModelForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            admission_number=form_data.cleaned_data.get('admission_number')
            name=form_data.cleaned_data.get('name')
            place=form_data.cleaned_data.get('place')
            age=form_data.cleaned_data.get('age')
            department= form_data.cleaned_data.get('department')
            phone_number= form_data.cleaned_data.get('phone_number')
            email= form_data.cleaned_data.get('email')
            image= form_data.cleaned_data.get('image')
            Student.objects.create(admission_number=admission_number,name=name, place=place, age=age, department=department,phone_number=phone_number,email=email,image=image)
            messages.success(request,'Student added successfully')
            return redirect('dash')
        messages.error(request,'Failed to add student.')
        return render(request, 'addstudent.html', {'form': form_data})

class DeleteTaskView(View):
    def get(self,request,*args,**kw):
        sid=kw.get('id')
        stu=Student.objects.get(id=sid)
        stu.delete()
        messages.success(request, 'Student deleted successfully.')
        return redirect('dash')
    

# class EditTaskView(View):
#     def get(self,request,**kw):
#         sid=kw.get('id')
#         stu=Student.objects.get(id=sid)
#         form=StudentModelForm(initial={'admission_number':stu.admission_number,'name':stu.name,'place':stu.place,'age':stu.age,'department':stu.department,'phone_number':stu.phone_number,'email':stu.email,'image':stu.image})
#         return render(request,'edit.html',{'form':form})
    
#     def post(self,request,**kw):
#         formdata=StudentModelForm(data=request.POST, files=request.FILES)
#         sid=kw.get('id')
#         stu=Student.objects.get(id=sid)
#         if formdata.is_valid():
#             admission_number=formdata.changed_data.get('admission_number')
#             name = formdata.cleaned_data.get('name')
#             place = formdata.cleaned_data.get('place')
#             age= formdata.cleaned_data.get('age')
#             department= formdata.cleaned_data.get('department')
#             phone_number= formdata.cleaned_data.get('phone_number')
#             email= formdata.cleaned_data.get('email')
#             image= formdata.cleaned_data.get('image')
#             stu.admission_number=admission_number
#             stu.name=name
#             stu.place=place
#             stu.age=age
#             stu.department=department
#             stu.phone_number=phone_number
#             stu.email=email
#             stu.image=image
#             stu.save()
#             messages.success(request, 'Student details updated successfully.')
#             return redirect('dash')
#         messages.error(request, 'Failed to update student details.')
#         return render(request, 'edit.html', {'form': formdata})


class EditTaskView(View):
    def get(self, request, **kw):
        sid = kw.get('id')
        stu = Student.objects.get(id=sid)
        form = StudentModelForm(initial={
            'admission_number': stu.admission_number,
            'name': stu.name,
            'place': stu.place,
            'age': stu.age,
            'department': stu.department,
            'phone_number': stu.phone_number,
            'email': stu.email,
            'image': stu.image
        })
        return render(request, 'edit.html', {'form': form})
    
    def post(self, request, **kw):
        sid = kw.get('id')
        stu = Student.objects.get(id=sid)
        formdata = StudentModelForm(data=request.POST, files=request.FILES, instance=stu)

        if formdata.is_valid():
            admission_number = formdata.cleaned_data.get('admission_number')

            # Check if the new admission number is unique or the same as the current student's
            if Student.objects.filter(admission_number=admission_number).exclude(id=sid).exists():
                messages.error(request, 'Student with this Admission number already exists.')
                return render(request, 'edit.html', {'form': formdata})
            
            # Save the form, which will automatically update the student instance
            formdata.save()
            messages.success(request, 'Student details updated successfully.')
            return redirect('dash')
        
        messages.error(request, 'Failed to update student details.')
        return render(request, 'edit.html', {'form': formdata})