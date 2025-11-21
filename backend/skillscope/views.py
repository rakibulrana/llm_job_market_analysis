from django.http import JsonResponse


def home(request):
    return JsonResponse(
        {
            "project": "SkillScope",
            "status": "running",
            "api_root": "/api/",
            "message": "Welcome to the SkillScope API backend",
        }
    )
