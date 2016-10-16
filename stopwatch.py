import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

second = 0
minute = 0
m_second = 0

def tick():
    global second, m_second, minute
    m_second = m_second + 1

    if m_second % 10 == 0:
        second = second + 1

    if second > 0 and second % 60 == 0:
        minute = minute + 1

    if second == 60:
        second = second - 60

    if m_second == 100:
        m_second = m_second - 100

    return str(minute) + ":" + str(second) + "." + str(m_second)

def timer_start():
    timer.start()

def timer_stop():
    timer.stop()

def timer_reset():
    global second, m_second, minute
    timer.stop()

    second = 0
    minute = 0
    m_second = 0

def draw(canvas):
    canvas.draw_text(tick(), [100, 100], 30, 'Green')

frame = simplegui.create_frame('stopwatch', 300, 300)
frame.add_button('START', timer_start)
frame.add_button('STOP', timer_stop)
frame.add_button('RESET', timer_reset)
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.start()

