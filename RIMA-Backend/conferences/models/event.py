from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo)
from .author import Author

class Event(StructuredNode):
    conference_event_name_abbr = StringProperty()
    conference_event_url = StringProperty()

    authors = RelationshipTo(Author, 'has_author')