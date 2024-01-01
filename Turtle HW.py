import turtle

SCREEN_WIDTH = 1200
SCREEN_HEIGH = 700
HEADER_HEIGHT_OFFSET = 250
TURTLE_WIDTH_OFFSET = -200
DIAMETER = 40
OFFSET = 0
COLUMNS = 30
LINES = 10
MAIN_SCREEN = None
PLACES = []
BKG_COLOR = "#F3F5BB"
FREE_SEAT_COLOR = "#29A006"
SOLD_SEAT_COLOR = "#ED1D1A"
PEN_COLOR = "#EDB31A"

main_turtle = turtle.Turtle()
main_turtle.shape('blank')
text_turtle = turtle.Turtle()
text_turtle.shape('blank')
screen_text = turtle.Turtle()
screen_text.shape('blank')

def setup_screen():
    main_screen = turtle.Screen()
    main_screen.title("GOIT CINEMA")
    main_screen.setworldcoordinates(0, main_screen.window_height(), main_screen.window_width(), 0)
    main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGH)
    main_screen.bgcolor(BKG_COLOR)
    return main_screen

def draw_cinema_screen(main_window):
    main_window.tracer(False)
    screen_width = 0.9 * SCREEN_WIDTH
    screen_height = 0.1 * HEADER_HEIGHT_OFFSET
    screen_start_x = (SCREEN_WIDTH - screen_width) / 2 - 210
    screen_start_y = (HEADER_HEIGHT_OFFSET - screen_height) / 2 - 150
    main_turtle.penup()
    main_turtle.setpos(screen_start_x, screen_start_y)
    main_turtle.pendown()
    main_turtle.fillcolor("#020bf7")
    main_turtle.begin_fill()
    for _ in range(2):
        main_turtle.forward(screen_width)
        main_turtle.left(90)
        main_turtle.forward(screen_height)
        main_turtle.left(90)
    main_turtle.end_fill()
    text_x = SCREEN_WIDTH / 2 - 210
    text_y = -12
    screen_text.penup()
    screen_text.setpos(text_x, text_y)
    screen_text.color("black")
    screen_text.write("<<ЭКРАН>>", align="center", font=("vergana", 15))
    main_window.tracer(True)

def text_printer(main_screen):
    main_screen.tracer(False)
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.setpos(-220, 30)
    text_turtle.pendown()
    places_amount = 0
    for line in PLACES:
        places_amount += len(line)
    text_turtle.write(f"Количество мест: {places_amount}", font=("vergana", 28))
    sold_count = 0
    for y in range(LINES):
        for x in range(COLUMNS):
            _, _, state = PLACES[y][x]
            if state is True:
                sold_count += 1
    text_turtle.penup()
    text_turtle.setpos(-220, 60)
    text_turtle.pendown()
    text_turtle.write(f"Продано мест: {sold_count}", font=("vergana", 20))
    text_turtle.penup()
    text_turtle.setpos(-220, 90)
    text_turtle.pendown()
    text_turtle.write(f"Свободно: {places_amount - sold_count}", font=("vergana", 20))
    main_screen.tracer(True)

def draw_circle(main_screen, pos_x, pos_y, pen_color, fill_color):
    main_screen.tracer(False)
    main_turtle.pencolor(pen_color)
    main_turtle.fillcolor(fill_color)
    main_turtle.begin_fill()
    main_turtle.penup()
    render_pos_x = TURTLE_WIDTH_OFFSET + pos_x * (DIAMETER + OFFSET)
    render_pos_y = pos_y * (DIAMETER + OFFSET) + HEADER_HEIGHT_OFFSET
    main_turtle.setpos(render_pos_x, render_pos_y)
    main_turtle.pendown()
    main_turtle.circle(DIAMETER // 2)
    main_turtle.end_fill()
    main_screen.tracer(True)
    return (render_pos_x, render_pos_y)

def vec_len(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def on_click(x, y, order):
    print(f"{x}; {y}")
    for line in range(LINES):
        for column in range(COLUMNS):
            place_x, place_y, _ = PLACES[line][column]
            if vec_len(x, y, place_x, place_y) <= DIAMETER // 2:
                if order == True:
                    draw_circle(MAIN_SCREEN, column, line, "#050500", "#f50202")
                    PLACES[line][column] = (place_x, place_y, order)
                else:
                    draw_circle(MAIN_SCREEN, column, line, "#f4fc03", "#47f502")
                    PLACES[line][column] = (place_x, place_y, order)
                text_printer(MAIN_SCREEN)

def on_click_mouse_1(x, y):
    on_click(x, y, order=True)

def on_click_mouse_2(x, y):
    on_click(x, y, order=False)

def main():
    global MAIN_SCREEN
    MAIN_SCREEN = setup_screen()
    draw_cinema_screen(MAIN_SCREEN)
    for y in range(LINES):
        PLACES.append(list())
        for x in range(COLUMNS):
            render_pos_x, render_pos_y = draw_circle(MAIN_SCREEN, x, y, "#f4fc03", "#47f502")
            PLACES[y].append((render_pos_x, render_pos_y, False))
    text_printer(MAIN_SCREEN)

    MAIN_SCREEN.onclick(on_click_mouse_1, btn=1)
    MAIN_SCREEN.onclick(on_click_mouse_2, btn=3)
    MAIN_SCREEN.mainloop()
    
    #seats_to_save = []
    #for seat, status in seats.items():
        #row_number = row - int(seat[1] // cell_height)
        #seat_number = int(seat[0] // cell_width) + 1
        #result = f"Row {row_number:02d}, seat {seat_number:02d} - {status}"
        #seats_to_save.append(result)
    #seats_to_save.sort()
    
#file = open("seats.tex", "w")
#file.write('\n'.join(seats_to_save))
#file.close

if __name__ == "__main__":
    main()