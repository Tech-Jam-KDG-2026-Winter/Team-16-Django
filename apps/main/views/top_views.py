from django.shortcuts import render, redirect

def top(request):
    if request.user.is_authenticated:
        return redirect("post_list")
    return render(request, "main/top.html")