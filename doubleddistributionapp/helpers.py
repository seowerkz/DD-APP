from io import BytesIO
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.http import HttpResponse
from cgi import escape


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        if 'work_order' in context_dict:
            filename = context_dict['work_order'].unit_number
            if context_dict['work_order'].axon_number:
                filename += '-%s' % context_dict['work_order'].axon_number
            response['Content-Disposition'] = 'filename=%s.pdf' % filename
        return response
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def is_member(user, group_name):
    return user.groups.filter(name=group_name).exists() or user.is_superuser
