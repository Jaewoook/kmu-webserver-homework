from django.shortcuts import get_object_or_404, render

from ..models import Comment, CommentHistory


def comment_history(request, comment_id):
    """
    pybo 댓글 수정내역
    """
    comment_histories = CommentHistory.objects.filter(comment__id=comment_id).order_by("-create_date")
    context = {
        "comment_histories": comment_histories
    }
    return render(request, "pybo/comment_history.html", context)
