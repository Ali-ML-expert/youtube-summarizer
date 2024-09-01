from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SingleVideoForm, SearchForm
from .utils import get_video_info, generate_summary, summarize_search_results
from .models import VideoSummary
from .chroma_utils import store_video_data
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'summarizer/home.html')

@login_required
def single_video_summary(request):
    if request.method == "POST":
        form = SingleVideoForm(request.POST)
        if form.is_valid():
            video_url = form.cleaned_data["video_url"]
            try:
                video_info = get_video_info(video_url)
                logger.debug(f"Video info retrieved: {video_info}")
                text_to_summarize = f"Title: {video_info['title']}\n\nDescription: {video_info['description']}"
                summary = generate_summary(text_to_summarize)
                logger.debug(f"Summary generated: {summary}")
                
                video_summary = VideoSummary.objects.create(
                    user=request.user,
                    video_url=video_url,
                    video_title=video_info["title"],
                    summary=summary['full_summary'],
                    short_description=summary['short_description']
                )
                
                store_video_data(video_summary)
                
                logger.debug(f"Rendering template with summary: {summary}")
                return render(request, 'summarizer/single_video_summary.html', {'summary': summary, 'video': video_info})
            except Exception as e:
                logger.error(f"Error processing video {video_url}: {str(e)}", exc_info=True)
                return render(request, 'summarizer/single_video_summary.html', {'form': form, 'error': str(e)})
    else:
        form = SingleVideoForm()
    return render(request, 'summarizer/single_video_summary.html', {'form': form})

@login_required
def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            logger.info(f"Search query: {query}")
            return redirect('search_results', query=query)
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = SearchForm()
    return render(request, 'summarizer/search.html', {'form': form})

@login_required
def search_results(request, query):
    logger.info(f"Processing search results for query: {query}")
    try:
        summaries = summarize_search_results(query)
        logger.info(f"Found {len(summaries)} results")
        for summary in summaries:
            logger.debug(f"Summary: {summary}")
        return render(request, 'summarizer/search_results.html', {'summaries': summaries, 'query': query})
    except Exception as e:
        logger.error(f"Error processing search query {query}: {str(e)}", exc_info=True)
        return render(request, 'summarizer/search.html', {'form': SearchForm(), 'error': f"An error occurred: {str(e)}"})

@login_required
def history(request):
    summaries = VideoSummary.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'summarizer/history.html', {'summaries': summaries})

@login_required
def user_profile(request):
    return render(request, 'summarizer/user_profile.html')
