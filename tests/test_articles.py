from swg.render import render_article
from swg.articles import get_article_metadata,get_article_from_path
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
    
def temp_article_file(tmpdir):
    content = "Contenido de prueba"
    temp_file = tmpdir.join("temp_article.txt")
    temp_file.write(content)
    return str(temp_file)

def test_get_article_from_path(temp_article_file):
    result = get_article_from_path(temp_article_file)
    expected = "Contenido de prueba"
    assert result == expected
    
