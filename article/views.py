import sys
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from subprocess import run, PIPE
from article.models import Output
# from script import *

# Create your views here.
def home(request):
    context={}
    return render(request, 'article/home.html' , context)

def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(uploaded_file.name)
    return render(request, 'article/upload.html', context)


def external(request):
    if request.method=="POST":
        print("this is post")
        inp = request.POST['param']
        import nltk
        nltk.download('punkt')
        sentences = nltk.tokenize.sent_tokenize(inp)
        # out = run([sys.executable, "script.py", inp], shell=False, stdout=PIPE)
        # print(out.stdout)
        print("======================================")
        print("Sentences :")
        print("======================================")
        sentence_length = len(sentences)
        print(sentence_length)
        word_count = []

        for i in range(sentence_length):
            each_sentence = sentences[i]
            
            sum = 1
            print(each_sentence)
            for j in range(len(each_sentence)):
                # print(each_sentence[j])
                if each_sentence[j] == " ":
                    sum +=1
            word_count.append(sum)

        print(word_count)
        sum_word_count = 0
        for i in range(len(word_count)):
            sum_word_count+=word_count[i]

        avg = sum_word_count / (len(word_count))

        highlights = []
        for i in range(len(word_count)):
            if word_count[i] > avg:
                highlights.append(True)
            else:
                highlights.append(False)
        print(highlights)

        #Clearing the Database
        Output.objects.all().delete()

        for i in range(sentence_length):
            saving_db = Output(sentence = sentences[i], highlight=highlights[i])
            saving_db.save()    

        output_html = Output.objects.all()
    return render(request, 'article/output.html', {'data1':output_html})