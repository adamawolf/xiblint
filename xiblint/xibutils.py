

def get_view_user_defined_attr(view, key_path):
    attr = view.find("./userDefinedRuntimeAttributes/userDefinedRuntimeAttribute[@keyPath='{}']".format(key_path))
    return attr.get('value') if attr is not None else None


def view_accessibility_label(view):
    config = view.find("accessibility[@key='accessibilityConfiguration']")
    return config.get('label') if config is not None else None


def view_is_accessibility_element(view):
    is_element = view.find("accessibility[@key='accessibilityConfiguration']/bool[@key='isElement']")
    if is_element is None:
        return
    return is_element.get('value') == 'YES'