import pytest
from src.Stack.Stack_node import Stack_node
from src.Stack.Staсk_list import Stack_lst
from src.Stack.Stack_queue import Stack_q


def Stack_methods(StackClass):
    st = StackClass()
    assert st.is_empty()
    assert len(st) == 0
    st.push(5)
    st.push(2)
    st.push(8)
    st.push(1)
    assert not st.is_empty()
    assert len(st) == 4
    assert st.peek() == 1
    assert st.min() == 1
    assert st.pop() == 1
    assert st.min() == 2
    assert st.pop() == 8
    assert st.min() == 2
    assert st.pop() == 2
    assert st.min() == 5
    assert st.pop() == 5
    assert st.is_empty()
    assert len(st) == 0


def check_stack_errors(StackClass):
    st = StackClass()
    with pytest.raises(ValueError):
        st.pop()
    with pytest.raises(ValueError):
        st.peek()
    with pytest.raises(ValueError):
        st.min()


def test_stack_node():
    Stack_methods(Stack_node)
    check_stack_errors(Stack_node)


def test_stack_list():
    Stack_methods(Stack_lst)
    check_stack_errors(Stack_lst)


def test_stack_queue():
    Stack_methods(Stack_q)
    check_stack_errors(Stack_q)
