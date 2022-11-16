def slugify(instance,new_slug=None):
    if new_slug:
        klass = instance.__class__
        qs = klass.objects.all().filter(slug=new_slug)
        if qs.exist():
            new_slug = qs.first().slug
