# Create your views here.
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic


class IndexView(generic.ListView):
    # get the latest 5 information from the database
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # join the list
    # output = '.'.join([p.question_text for p in latest_question_list])

    # get a template from templates
    # template = loader.get_template('polls/index.html')

    # load the context as a RequestContext
    # context must be a dict
    # context = {'latest_question_list': latest_question_list, }
    #  return HttpResponse(template.render(context))
    #  return render(request, 'polls/index.html', context)
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """return the last five published question"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # if exception render to 404 page else render to detail.html
    # it is a shortcuts very simple
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/result.html', {'question': question})
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    #  return HttpResponse("You are voting on question %s" % question_id)
    p = get_object_or_404(Question, pk=question_id)
    try:
        # POST value is always strings
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'question': p,
                   'error_message': "You didnot select a choice", }
        return render(request, 'polls/detail.html', context)

    else:
        selected_choice.votes += 1
        selected_choice.save()
    # if success wo should  return an HttpResponseRedirect
    # we use reverse to reverse the name 'polls:result' and args to url like
    # '/polls/3/result'
    return HttpResponseRedirect(reverse('polls:result', args=(p.id, )))
