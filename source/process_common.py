def convert_to_identifier_with_no_lowercase(s0):
    for string in (' ', "'", "`", "(", ")", "-", "\t"):
        s0 = s0.replace(string, '_')
    for string in (",", "|"):
        s0 = s0.replace(string, '')
    return s0


def convert_to_identifier(s0):
    return convert_to_identifier_with_no_lowercase(s0).lower()


def replace_spaces(s0):
    return s0.replace("\t", "_").replace(" ", "_")
