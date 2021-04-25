context = {}


def set_options(args):
    context["options"] = vars(args)


def get_option(key: str):
    return context["options"][key]
