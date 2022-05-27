from pathlib import Path
from subprocess import check_call

import markdown
import mkepub
from mkepub.mkepub import Book

from .constants import DOCS, EPUB_AUTHOR, EPUB_FILE, EPUB_TITLE, TITLE_REGEXP


def add_page(book: Book, path: Path) -> None:
    html = convert(path)
    title = extract_title(html)
    print(f"{title}")
    book.add_page(title=title, content=html)


def convert(path: Path) -> str:
    return markdown.markdown(
        path.read_text(),
        extensions=["pymdownx.superfences"],
        output_format="xhtml",
    )


def extract_title(html: str) -> str:
    return TITLE_REGEXP.findall(html)[0]


def make_it() -> None:
    book = mkepub.Book(title=EPUB_TITLE, author=EPUB_AUTHOR)

    # with Path("cover.jpg").open(mode="rb") as fh:
    #     book.set_cover(fh.read())

    for page in sorted(DOCS.glob("*.md")):
        add_page(book, page)

    EPUB_FILE.parent.mkdir(exist_ok=True)
    EPUB_FILE.unlink(missing_ok=True)
    book.save(EPUB_FILE)

    # Check
    check_call(["epubcheck", str(EPUB_FILE)])
