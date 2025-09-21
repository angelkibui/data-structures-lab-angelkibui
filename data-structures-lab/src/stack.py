"""
Stack Implementation - Last In, First Out (LIFO)
Enterprise Use Case: Browser back button, undo operations
"""

class Stack:
    def __init__(self):
        """Initialize empty stack using Python list."""
        self.items = []  # This is where we store our items
    
    def push(self, item):
        """
        Add item to top of stack.
        Time Complexity: O(1) - Super fast!
        
        Args:
            item: Element to add to stack
        """
        self.items.append(item)  # Just add to the end!
    
    def pop(self):
        """
        Remove and return top item from stack.
        Time Complexity: O(1) - Super fast!
        
        Returns:
            Top item from stack
        
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack!")
        return self.items.pop()  # Remove from the end!
    
    def peek(self):
        """
        Return top item without removing it.
        Time Complexity: O(1) - Super fast!
        
        Returns:
            Top item from stack
        
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty stack!")
        return self.items[-1]  # Look at the last item!
    
    def is_empty(self):
        """
        Check if stack is empty.
        Time Complexity: O(1) - Super fast!
        
        Returns:
            bool: True if stack is empty, False otherwise
        """
        return len(self.items) == 0  # Check if list is empty!
    
    def size(self):
        """
        Get number of items in stack.
        Time Complexity: O(1) - Super fast!
        
        Returns:
            int: Number of items in stack
        """
        return len(self.items)  # Just return the length!
    
    def __str__(self):
        """String representation of stack (top to bottom)."""
        return f"Stack({self.items})"  # Show our items!