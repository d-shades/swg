import markdown
import os


def get_article_metadata(article: str) -> dict:
    md = markdown.Markdown(extensions=["full_yaml_metadata"])
    md.convert(article)
    return md.Meta

def get_all_articles_path_from_dir(dirpath: str) -> list[str]:
    articles_path = []
    for filename in os.listdir(dirpath):
        filepath = os.path.join(dirpath, filename)
        if os.path.isfile(filepath):
            articles_path.append(filepath)
    return articles_path