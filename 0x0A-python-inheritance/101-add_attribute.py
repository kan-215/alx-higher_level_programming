def add_attribute(obj, name, value):
    """Add attributes to object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
