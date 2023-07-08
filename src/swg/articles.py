import markdown


def get_article_metadata(article: str) -> dict:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])
    md.convert(article)
    return md.Meta

def get_article_body(article: str) -> str:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])
    md.convert(article)
    return md.Body