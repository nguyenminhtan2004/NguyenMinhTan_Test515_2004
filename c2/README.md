# Câu 02 - PlayFair UI Qt Designer + API

Bản này làm theo kiểu Câu 3:
- Giao diện đơn giản, không style màu mè.
- Có file `ui/playfair.ui` mở được bằng Qt Designer.
- Có file `api.py` riêng để xử lý API.
- File chạy giao diện là `playfair_cipher.py`.

## Cấu trúc

```text
c2
├── api.py
├── playfair_cipher.py
├── requirement.txt
├── requirements.txt
├── run_api.bat
├── run_ui.bat
├── cipher
│   └── playfair
│       ├── __init__.py
│       └── playfair_cipher.py
└── ui
    ├── playfair.ui
    └── playfair.py
```

## Cài thư viện

```bash
cd c2
python -m pip install -r requirement.txt
```

## Chạy bài

Mở terminal 1:

```bash
cd c2
python api.py
```

Mở terminal 2:

```bash
cd c2
python playfair_cipher.py
```

Hoặc bấm lần lượt:

```text
run_api.bat
run_ui.bat
```

## Test mẫu

Key:

```text
MONARCHY
```

Input:

```text
INSTRUMENTS
```

Bấm Encrypt, kết quả đúng:

```text
GATLMZCLRQXA
```

Sau đó copy `GATLMZCLRQXA` vào ô Input, bấm Decrypt.

## Mở bằng Qt Designer

Mở file:

```text
ui/playfair.ui
```

Nếu sửa giao diện trong Qt Designer, sinh lại file Python:

```bash
pyuic5 ui/playfair.ui -o ui/playfair.py
```

## Commit

```bash
git add c2
git commit -m "Cau 02: Them UI PlayFair Qt Designer va API"
git push origin Tuan6
```
