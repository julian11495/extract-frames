import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def seleccionar_carpeta():
    ruta_carpeta = filedialog.askdirectory()
    entry_ruta_guardado.delete(0, tk.END)
    entry_ruta_guardado.insert(0, ruta_carpeta)

def mostrar_procesamiento_finalizado():
    messagebox.showinfo("Procesamiento Finalizado", "El procesamiento del video ha finalizado correctamente.")

def extraer_imagenes(video_path, tiempo_captura_ms, ruta_guardado, identificador):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)

    tiempo_frame = tiempo_captura_ms * 0.001 * fps
    frame_counter = 0

    while True:
        video.set(cv2.CAP_PROP_POS_FRAMES, int(tiempo_frame * frame_counter))
        ret, frame = video.read()

        if ret:
            if identificador:
                nombre_imagen = f"{ruta_guardado}/{identificador}_frame_{frame_counter}_{tiempo_captura_ms}ms.jpg"
            else:
                nombre_imagen = f"{ruta_guardado}/frame_{frame_counter}_{tiempo_captura_ms}ms.jpg"
            
            cv2.imwrite(nombre_imagen, frame)
            print(f"Imagen guardada: {nombre_imagen}")
            frame_counter += 1
        else:
            break

    video.release()
    mostrar_procesamiento_finalizado()

def cargar_video():
    ruta_video = filedialog.askopenfilename(filetypes=[("Archivo de video", "*.mp4")])
    entry_ruta_video.delete(0, tk.END)
    entry_ruta_video.insert(0, ruta_video)

def procesar_video():
    ruta_video = entry_ruta_video.get()
    tiempo_captura_ms = int(entry_tiempo_ms.get())
    ruta_guardado = entry_ruta_guardado.get()
    identificador = entry_identificador.get()  # Nuevo campo de entrada para el identificador

    extraer_imagenes(ruta_video, tiempo_captura_ms, ruta_guardado, identificador)

# Crear la ventana
root = tk.Tk()
root.title("Extractor de Imágenes de Video")

# Crear y posicionar los elementos en la ventana
label_ruta_video = tk.Label(root, text="Ruta del video:")
label_ruta_video.grid(row=0, column=0)

entry_ruta_video = tk.Entry(root, width=50)
entry_ruta_video.grid(row=0, column=1)

btn_cargar_video = tk.Button(root, text="Cargar Video", command=cargar_video)
btn_cargar_video.grid(row=0, column=2)

label_tiempo_ms = tk.Label(root, text="Tiempo de captura (ms):")
label_tiempo_ms.grid(row=1, column=0)

entry_tiempo_ms = tk.Entry(root, width=10)
entry_tiempo_ms.grid(row=1, column=1)

label_ruta_guardado = tk.Label(root, text="Ruta de guardado:")
label_ruta_guardado.grid(row=2, column=0)

entry_ruta_guardado = tk.Entry(root, width=50)
entry_ruta_guardado.grid(row=2, column=1)

label_identificador = tk.Label(root, text="Identificador:")
label_identificador.grid(row=3, column=0)

entry_identificador = tk.Entry(root, width=10)
entry_identificador.grid(row=3, column=1)

btn_seleccionar_carpeta = tk.Button(root, text="Seleccionar Carpeta", command=seleccionar_carpeta)
btn_seleccionar_carpeta.grid(row=2, column=2)

btn_procesar = tk.Button(root, text="Procesar", command=procesar_video)
btn_procesar.grid(row=4, column=1)

# Iniciar la ventana
root.mainloop()
