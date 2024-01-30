# Aplicación python para extraer frames en formato jpg a partir de videos MP4 cada x tiempo definido por el usuario

1. Instalar Anaconda desde https://www.anaconda.com/download
3. Crear un entorno con python 3.10
4. Abrir la terminal de comando del entorno creado
5. Instalar opencv usando el comando: `pip install opencv-python`
6. Intalar ffmpeg usando el comando: `conda install anaconda::ffmpeg`
7. Descarga el fichero disponible en este repositorio: `Extraer_frames.py`
8. Desde la terminal de comandos del entorno creado en conda y en la ubicación de descarga correspondiente del fichero descargado conforme el apartado 6, ejecutar `python Extraer_frames.py`
9. Se abrirá la aplicación mostrada a continuación donde se deben indicar los parámetros de entrada correspondientes.
   
![1](https://github.com/julian11495/extract-frames/assets/32869939/323319f3-d577-478d-9c11-c210406c8425)

6. Una vez introducidos los datos de entrada anteriores, se debe oprimir `Procesar` y el se generarán las automáticamenbte imágenes en formato JPG en la carpeta de salida proporcionada.
7. Para los datos de ejemplo del paso 4, el formato de la imagen es `Coche_12_frame_1_500ms.jpg`: en donde Coche_12 corresponde al identificador suministrado, posteriormente el número de frame extraido y el dato final indica el tiempo de muestreo seleccionado.
8. Al finalizar el procesamiento y extracción de imágenes del video se mostrará el siguiente mensaje:

![2](https://github.com/julian11495/extract-frames/assets/32869939/32bbe40b-fcf3-476e-a51f-c379bffe2874)





