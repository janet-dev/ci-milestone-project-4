from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    This Python code defines a custom widget called CustomClearableFileInput
    for handling file inputs in Django forms. It extends the default
    ClearableFileInput widget and customizes some of its attributes.
    gettext_lazy function is used for label translation into other languages.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name \
        = 'products/custom_widget_templates/custom_clearable_file_input.html'
