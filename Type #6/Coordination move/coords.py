import turtle as t  # Подключим модуль черепашка

t.color("black", "red")

k = 10
t.speed(100000)
t.setx(0)
t.sety(0)
for i in range(7):  # пропишем алгоритм построения фигуры по условию
    t.setx(t.xcor() + 6 * k)
    t.sety(t.ycor() - 9 * k)
    t.setx(t.xcor() - 6 * k)
    t.sety(t.ycor() + 2 * k)
    t.setx(t.xcor() + 12 * k)
    t.sety(t.ycor() + 3 * k)

t.up()
t.speed(10)  # Увеличим скорость черепашки
for x in range(15 * k):  # Алгоритм построения точек
    for y in range(-5 * k, 15 * k):
        t.goto(x * k, y * k)
        t.dot(4)  # точки размером 4 пикселя
t.done()
