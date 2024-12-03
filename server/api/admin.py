from django.contrib import admin
from .models import (
    User, BlogPost, Comment, CommentReply, PostLike, 
    Tag, PostTag, Notification, Follow, Bookmark, 
    ReportBlog, ReportComment, ReportCommentReply, ReportUser
)

# Đăng ký từng model vào admin
admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(PostLike)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(Notification)
admin.site.register(Follow)
admin.site.register(Bookmark)
admin.site.register(ReportBlog)
admin.site.register(ReportComment)
admin.site.register(ReportCommentReply)
admin.site.register(ReportUser)
