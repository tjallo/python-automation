import wikipedia

string_parser = lambda input_string: input_string if len(input_string) <= 1995 else input_string[:1995] + "..."

def get_summary(article_name):
    summary = wikipedia.summary(article_name)
    result = string_parser(summary)
    return result
