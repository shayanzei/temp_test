from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

def handle_soft_delete(request, model_class, object_id, success_url_name,
                       template_name=None):
    """
    Generic helper for handling soft deletes with dynamic templates.

    Parameters:
    - request: The HttpRequest object.
    - model_class: The model class of the object to delete.
    - object_id: The primary key of the object to delete.
    - success_url_name: The name of the URL to redirect to upon success.
    - template_name: Optional. The template to render for confirmation.
                     Defaults to '<app_label>/<model_name>_confirm_delete.html'.

    Returns:
    - HttpResponse: Redirect after marking the object as deleted or rendering the confirmation page.
    """
    obj = get_object_or_404(model_class, id=object_id)

    # Infer default template name dynamically if not provided - may need to delete this!
    if not template_name:
        app_label = model_class._meta.app_label
        model_name = model_class._meta.model_name
        template_name = f"{app_label}/{model_name}_confirm_delete.html"

    if request.method == 'POST':
        obj.is_deleted = True
        obj.save()
        return redirect(reverse(success_url_name))

    return render(request, template_name, {'object': obj})
