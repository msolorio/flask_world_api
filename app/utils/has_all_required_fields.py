def has_all_required_fields(data, fields):
    missing_fields = []

    for field in fields:
        if not data.get(field):
            missing_fields.append(field)

    if missing_fields:
        return False, missing_fields
    
    return True, None