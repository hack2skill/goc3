from datetime import datetime as dt


def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return dt_.strftime(fmt)


# def now(fmt="%X"):
#     return format_date(dt.now(), fmt[:-3])
def now(fmt="%X"):
    return format_date(dt.now(), fmt)[:-3]


def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(el, class_name):
    el.classList.add(class_name)


def add_classes(element, class_list):
    for klass in class_list.split(" "):
        element.classList.add(klass)
