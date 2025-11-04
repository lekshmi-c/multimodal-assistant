# 🧠 Multimodal Assistant

A **privacy-focused**, **locally-run AI assistant** that understands **both text and images**—all on your machine, with **no external APIs** or cloud dependencies. Built with **Streamlit**, **FastAPI**, **Ollama (LLaMA2)**, and **Tesseract OCR**, this tool lets you:
- Ask questions in natural language, **or**
- Upload images (e.g., screenshots, flyers, handwritten notes) and get intelligent summaries of the text they contain.

Perfect for researchers, students, or anyone working with mixed-media content offline.

---

## 🔍 Problem Solved

Most AI assistants handle **only text** _or_ **only images**. The **Multimodal Assistant** bridges this gap by:
- Processing **text queries** using a local LLM (LLaMA2 via Ollama),
- Extracting text from **uploaded images** using OCR,
- Summarizing or answering based on **both modalities** through the same intelligent backend.

---

## 🛠️ Tech Stack

| Component        | Technology                      |
|------------------|---------------------------------|
| **Frontend**     | Streamlit                       |
| **Backend**      | FastAPI                         |
| **LLM Engine**   | Ollama + `llama2`               |
| **OCR**          | `pytesseract` + Tesseract-OCR   |
| **Image Handling**| Pillow (PIL)                   |
| **HTTP Client**  | `requests`                      |

---

## 📂 Project Structure

```
multimodal-assistant/
├── backend/
│   ├── main.py                 # FastAPI app entrypoint
│   ├── routes.py               # API routes
│   ├── services/
│   │   ├── text_handler.py     # Text query logic
│   │   └── image_handler.py    # OCR + image processing
│   └── models/
│       └── llm_model.py        # Ollama integration
├── frontend/
│   └── app.py                  # Streamlit UI
├── .env                        # Environment variables (optional)
└── requirements.txt            # Python dependencies
```

---

## ⚙️ Prerequisites

1. **Python 3.10+**
2. **Ollama** – [Install from ollama.com](https://ollama.com)
3. **Tesseract-OCR** – [Download & install](https://github.com/tesseract-ocr/tesseract), and **add to your system PATH**
4. **LLaMA2 model** pulled locally:
   ```bash
   ollama pull llama2
   ```

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/lekshmi-c/multimodal-assistant.git
cd multimodal-assistant

# Create virtual environment
python -m venv .venv

# Activate it
.venv\Scripts\activate      # Windows
# or
source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the App

> Open **two terminal windows**.

**Terminal 1 – Start Backend (FastAPI):**
```bash
cd backend
uvicorn main:app --reload
```
> API will run at: `http://localhost:8000`

**Terminal 2 – Start Frontend (Streamlit):**
```bash
cd frontend
streamlit run app.py
```
> UI will open at: `http://localhost:8501`

> 💡 Make sure Ollama is running and `llama2` is available.

---

## 🧪 How to Use

### 📝 Text Mode
1. Type a question like:  
   _"What are the benefits of open-source LLMs?"_
2. Click **Submit**.
3. Get a concise, intelligent response from LLaMA2.

### 🖼️ Image Mode
1. Upload an image containing text (e.g., a screenshot, poster, or handwritten note).
2. The app:
   - Uses **Tesseract OCR** to extract text,
   - Sends it to **LLaMA2** via Ollama for summarization or analysis.
3. View the AI-generated insight in the chat panel.

---

## ⚠️ Configuration Notes

### Tesseract Path (Windows)
Update the path in `backend/services/image_handler.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
> On macOS/Linux, this is usually auto-detected if Tesseract is in your PATH.

---

## ✨ Key Features

- **Dual Modality Support**: Text + image input in one interface.
- **100% Local**: No data leaves your machine.
- **Offline After Setup**: No internet required post-installation.
- **Extensible Architecture**: Modular backend for future enhancements (e.g., audio, captioning).

---

## 🔮 Future Enhancements

- 🎨 **Image captioning** with BLIP or CLIP
- 🎤 **Voice input** via Whisper
- 💾 **Chat history** & memory persistence
- 🐳 **Docker containerization** for easy deployment

---

## 🧾 License

This project is open-source. See the repository for license details.

---

> 💡 **Tip**: Ideal for analyzing printed documents, social media screenshots, lecture slides, or any visual content that contains text—without manual transcription!
