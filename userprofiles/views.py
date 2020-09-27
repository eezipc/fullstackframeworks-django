from django.shortcuts import render


def userprofileview(request):
    """ Display the user's profile. """

    template = 'userprofiles/userprofile.html'
    context = {}

    return render(request, template, context)