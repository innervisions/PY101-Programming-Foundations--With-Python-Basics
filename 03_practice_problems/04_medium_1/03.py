def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# The first function (add_to_rolling_buffer1) mutates the original list represented by buffer.
# The second function (add_to_rolling_buffer2) does not mutate the original list,
# but instead creates a new list and assigns it to buffer, whose value ultimately
# gets returned by the function.
