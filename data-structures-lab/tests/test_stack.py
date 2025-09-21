import pytest
from src.stack import Stack

class TestStack:
    def test_push_and_size(self):
        """Test pushing elements increases size correctly."""
        stack = Stack()
        assert stack.size() == 0
        
        stack.push(1)
        assert stack.size() == 1
        
        stack.push(2)
        assert stack.size() == 2
    
    def test_pop_lifo_order(self):
        """Test that pop follows Last In, First Out order."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.pop() == 3  # Last in, first out!
        assert stack.pop() == 2
        assert stack.pop() == 1
    
    def test_empty_stack_operations(self):
        """Test operations on empty stack raise appropriate errors."""
        stack = Stack()
        
        # Test pop on empty stack
        with pytest.raises(IndexError):
            stack.pop()
        
        # Test peek on empty stack  
        with pytest.raises(IndexError):
            stack.peek()
    
    def test_peek(self):
        """Test that peek returns top without removing."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        
        assert stack.peek() == 2  # Should see 2
        assert stack.size() == 2  # Size shouldn't change!
        assert stack.pop() == 2   # Now remove it
    
    def test_is_empty(self):
        """Test is_empty method."""
        stack = Stack()
        assert stack.is_empty() == True
        
        stack.push(1)
        assert stack.is_empty() == False
        
        stack.pop()
        assert stack.is_empty() == True
    
    def test_string_representation(self):
        """Test string representation."""
        stack = Stack()
        assert str(stack) == "Stack([])"
        
        stack.push(1)
        assert str(stack) == "Stack([1])"
        
        stack.push(2)
        assert str(stack) == "Stack([1, 2])"