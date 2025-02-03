#!/usr/bin/python3
"""
This module implements a verbose list that prints notifications
when items are added or removed.
"""

class VerboseList(list):
   """A list subclass that prints notifications for modifications."""
   
   def append(self, item):
       """Add item to end of list with notification."""
       super().append(item)
       print(f"Added [{item}] to the list.")

   def extend(self, items):
       """Extend list with items and print notification."""
       super().extend(items)
       print(f"Extended the list with [{len(items)}] items.")

   def remove(self, item):
       """Remove first occurrence of item with notification."""
       super().remove(item)
       print(f"Removed [{item}] from the list.")

   def pop(self, index=-1):
       """Remove and return item at index with notification."""
       item = super().pop(index)
       print(f"Popped [{item}] from the list.")
       return item
