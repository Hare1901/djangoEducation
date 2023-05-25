class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):

        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['totle'] = self.title

        return context