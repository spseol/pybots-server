from flask.globals import request


def form_to_kwargs(origin_view):
    def view(*args, **kwargs):
        kwargs.update(request.form.items())
        return origin_view(*args, **kwargs)

    return view


def args_to_kwargs(origin_view):
    def view(*args, **kwargs):
        kwargs.update(request.args.items())
        return origin_view(*args, **kwargs)

    return view
