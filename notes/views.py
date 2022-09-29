from django.shortcuts import redirect, render
# from .filters import NotesFilter
from .models import *
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .forms import NoteCreationForm

#pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    notes = Note.objects.filter(title__icontains=q)
    notes_count = notes.count()
    # myFilter  = NotesFilter(request.GET, queryset = notes)
    # notes = myFilter.qs
    page = request.GET.get('page', 1)

    paginator = Paginator(notes, 2)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes= paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    context={
        'notes':notes,
        'notes_count':notes_count
    }
    return render(request,'notes/index.html',context)

def NoteDetail(request,pk):
    note = Note.objects.get(id=pk)
    context={
        'note':note,

    }
    return render (request, 'notes/detail.html', context)

# class NoteCreateView(CreateView):
#     model = Note
#     # success_url = 'detail'
#     template_name = 'notes/new_note.html'
#     fields = ['title','description']

def NoteCreate(request):
    form = NoteCreationForm()
    if request.method=='POST':
        form = NoteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form 
    }
    return render(request,'notes/new_note.html', context)

class NoteUpdateView(UpdateView):
    model = Note
    # success_url = 'detail'
    template_name = 'notes/new_note.html'
    fields = ['title','description']

class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/'
    template_name = 'notes/note_delete_confirm.html'
    fields = ['title','description']
