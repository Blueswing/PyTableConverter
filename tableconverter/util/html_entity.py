import os.path
import json

with open(os.path.join(os.path.dirname(__file__), "html_entity.json")) as f:
    txt = f.read()
HTML_ENTITY_MAP = json.loads(txt)
REVERSE_ENTITY_MAP = dict((v, k) for k, v in HTML_ENTITY_MAP.items())


def convert_char_to_html_entity(ch: str) -> str:
    if ch in HTML_ENTITY_MAP:
        ch = HTML_ENTITY_MAP[ch]
    return ch


def convert_html_entity_to_char(entity: str) -> str:
    if entity in REVERSE_ENTITY_MAP:
        entity = REVERSE_ENTITY_MAP[entity]
    return entity
