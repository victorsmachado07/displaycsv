from flask import Flask, request, render_template
import pandas as pd
import io
import chardet   # Biblioteca para detectar encoding

app = Flask(__name__)

def detectar_encoding(file_bytes):
    """Detecta automaticamente o encoding do arquivo."""
    det = chardet.detect(file_bytes)
    return det["encoding"] if det["encoding"] else "utf-8"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display', methods=['POST'])
def display_file():
    file = request.files.get('file')

    if not file or file.filename == "":
        return "Nenhum arquivo enviado."

    try:
        # Primeiro lemos os bytes para detectar encoding
        file_bytes = file.read()
        encoding = detectar_encoding(file_bytes)

        # Depois reposicionamos o ponteiro para o início
        file.stream.seek(0)

        # Leitura automática do separador
        # sep=None + engine="python" => Pandas detecta automaticamente
        df = pd.read_csv(
            io.BytesIO(file_bytes),
            sep=None,               # Detecta automático ( ; , | \t )
            engine="python",
            encoding=encoding
        )

    except Exception as e:
        return f"Erro ao processar o CSV: {e}"

    # Renderiza no template com a classe da tabela definida no HTML
    return render_template(
        'display.html',
        tables=[df.to_html(classes='data', index=False)],
        titles=df.columns.values
    )


if __name__ == '__main__':
    app.run(debug=True)
