from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3

class MyGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Cargar el modelo (un panda) y colocarlo en la escena
        self.model = self.loader.loadModel("models/panda-model")
        self.model.reparentTo(self.render)

        # Cambiar la posición del modelo
        self.model.setPos(Point3(0, 50, 0))

        # Configurar cámara
        self.camera.setPos(0, -100, 10)
        self.camera.lookAt(self.model)

# Crear instancia del juego y ejecutarlo
game = MyGame()
game.run()
