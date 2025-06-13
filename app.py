import whisper
import gradio as gr

modelo = whisper.load_model("base")

def transcribir(audio):
    if audio is None:
        return "No se subió ningún archivo."
    resultado = modelo.transcribe(audio, language="es")
    return resultado["text"]

interfaz = gr.Interface(
    fn=transcribir,
    inputs=gr.Audio(source="upload", type="filepath", label="Sube tu audio"),
    outputs="text",
    title="Transcriptor en Español",
    description="Sube tu audio en español (largo o corto) y recibe la transcripción automática."
)

interfaz.launch()
