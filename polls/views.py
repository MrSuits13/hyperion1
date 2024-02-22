from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required  # Importing the login_required decorator
from .models import Question, Choice

def index(request):
    """
    View function for the index page.

    This view retrieves the latest 5 questions from the database and renders the poll.html template with the retrieved questions.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse object with the rendered HTML content.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list': latest_question_list}
    return render(request, 'polls/poll.html', context)

def detail(request, question_id):
    """
    View function for the detail page of a question.

    This view retrieves the question object with the given question_id from the database and renders the detail.html template with the question details.

    Args:
        request: HttpRequest object.
        question_id: ID of the question to be displayed.

    Returns:
        HttpResponse object with the rendered HTML content.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    View function for the results page of a question.

    This view retrieves the question object with the given question_id from the database and renders the results.html template with the question results.

    Args:
        request: HttpRequest object.
        question_id: ID of the question whose results are to be displayed.

    Returns:
        HttpResponse object with the rendered HTML content.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required  # Appling the decorator to restrict access to authenticated users only
def vote(request, question_id):
    """
    View function for voting on a question.

    This view handles the voting process for a question. It retrieves the selected choice from the request and increments its vote count. It then redirects to the results page of the question.

    Args:
        request: HttpRequest object.
        question_id: ID of the question being voted on.

    Returns:
        HttpResponseRedirect object redirecting to the results page of the question.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
