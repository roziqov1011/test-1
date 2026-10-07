# Strands Decider 2B — test-1

Amazon Web Services (AWS) Strands Decider 2B bilan tajriba qilish uchun tayyor loyiha.

## Nima qiladi?

Decider generativ chatbot emas. U berilgan holat (state) asosida oldindan berilgan variantlardan tanlaydi va qaror ishonchliligini qaytaradi.

## O'rnatish

Python 3.10+ tavsiya qilinadi:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate

pip install -r requirements.txt
```

## Ishga tushirish

```bash
python app.py
```

Yoki Windows'da:

```text
run.bat
```

## Muhim

Modelni yuklash/ishga tushirish uchun internet va Hugging Face model access kerak bo'lishi mumkin. Model nomi `StrandsAgents/strands-decider-2B-hobson-v21` sifatida sozlangan.

Bu loyiha Decider'ni agent ichida ishlatish uchun minimal boshlang'ich skeleton hisoblanadi.
