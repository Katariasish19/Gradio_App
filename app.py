import gradio as gr
from backend import generate_documentation  # Import the backend function

def process_csharp_code(file):
    """
    Wrapper for processing C# code file and returning generated documentation.
    """
    return generate_documentation(file)

# Gradio Interface
ui = gr.Interface(
    fn=process_csharp_code,
    inputs=gr.File(label="Upload C# File", type="filepath"),
    outputs=gr.Textbox(label="Generated Documentation"),
    title="C# Code Documentation Generator"
)

if __name__ == "__main__":
    ui.launch()
