import markdown


def get_article_metadata(article: str) -> dict:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])
    md.convert(article)
    return md.Meta


def get_article_from_path(path: str) -> str:
    with open(path,"r") as art:
        text = art.read()
        return text