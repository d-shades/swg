from swg.render import render_article
from swg.articles import get_article_metadata, get_article_body
from swg import settings
import os
from pathlib import Path

import pytest

@pytest.fixture
def current_working_directory():
    return settings.CURRENT_WORKING_DIR


def test_exists_blog_article_template(current_working_directory):
    assert os.path.exists(
        Path(current_working_directory) / "templates" / "default" / "post.html")


def test_get_article_metadata():
    test_article = "---\narticle_title: titulo"
    test_article += "\narticle_subtitle: subtitulo"
    test_article += "\n---\ntext\n"

    metadata = get_article_metadata(test_article)
    assert "article_title" in metadata
    assert "article_subtitle" in metadata
    assert metadata["article_title"] == "titulo"
    assert metadata["article_subtitle"] == "subtitulo"
 
def test_get_article_body():
    """
    Function get_article_body should return expected string corresponding to the article's body
    """
    test_article = """
        ---
        title: Example Article
        date: 2023-07-08
        ---
        
        This is the body of the article.
        """

    expected_body = "This is the body of the article."

    gathered_body = get_article_body(test_article)

    assert expected_body == gathered_body


