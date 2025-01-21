from libs import Canvas, Population

canva = Canvas()
population = Population()

while canva.running:
    canva.event()
    canva.clear()
    
    population.draw(canva.screen)
    population.update()

    canva.update()