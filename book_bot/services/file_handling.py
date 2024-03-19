import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punctuation = (',.!:;?')

    if start + size >= len(text):
        size = len(text) - start

    if start + size != len(text):
        while text[start + size] in punctuation:
            size -= 1
    out_text = text[start:start + size]

    for c in range(len(out_text)-1, 0, -1):
        if out_text[c] in punctuation:
            break
    out_text = out_text[:c+1]
    out_size = len(out_text)

    return (out_text, out_size)


def prepare_book(path: str) -> None:
    txt = ''
    with open('book.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
    start = 0
    q = 1
    while txt:
        book[q], w = _get_part_text(txt, start, PAGE_SIZE)
        book[q] = book[q].strip()
        txt = txt[w:]
        q += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
