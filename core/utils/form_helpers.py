from django.shortcuts import render, redirect
from django.urls import reverse

def handle_form(request, form_class, template_name, instance=None,
                success_url_name=None, extra_context=None):
    """
    Generic helper for handling forms in create and update views.

    Parameters:
    - request: The HttpRequest object.
    - form_class: The form class to use.
    - template_name: Template to render for the form.
    - instance: The model instance to update (optional).
    - success_url_name: The name of the URL to redirect to upon success.
    - extra_context: Additional context to pass to the template.

    Returns:
    - HttpResponse: Either a redirect or a rendered form template.
    """
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            if hasattr(obj, 'created_by') and not instance:  # Set created_by for new objects
                obj.created_by = request.user
            obj.save()
            return redirect(
                reverse(success_url_name,
                        kwargs={'project_id': obj.id if hasattr(obj, 'id') else None}))
    else:
        form = form_class(instance=instance)

    context = {'form': form}
    if extra_context:
        context.update(extra_context)
    return render(request, template_name, context)
