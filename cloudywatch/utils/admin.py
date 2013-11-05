from django.core.urlresolvers import reverse


def get_admin_add_link(cls):
    opts = cls._meta
    return reverse('admin:%s_%s_add' % (opts.app_label, opts.module_name))
