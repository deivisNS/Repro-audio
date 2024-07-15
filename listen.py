import pyglet


def listen_audio(audio):
	
	if audio.endswith(".mp3"):

		#indicamos cual audio queremos reproducir
		source = pyglet.media.load(audio, streaming = True)

		repro(source)


def repro(audio):

	#para poder controlar el audio. poder poner pause y play
	player = pyglet.media.Player()

	#evento para cuando el audio termine
	def on_eos():
		
		#una vez terminado el audio, lo pausamos
		player.pause()

		#eliminamos el audio de la memoria para poder liberar recursos
		player.delete()

		#cerramos el programa
		pyglet.app.exit()
	
	#agregamos el evento al controlador
	player.on_eos = on_eos

	#indicamos cual audio sera controlado
	player.queue(audio)

	#comenzamos la reproduccion
	player.play()

	#para que tenga en cuenta los eventos
	pyglet.app.run()


listen_audio("saludo.mp3")