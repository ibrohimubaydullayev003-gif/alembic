# FastAPI + Alembic migration project

Ushbu loyiha FastAPI, SQLAlchemy va Alembic yordamida ma'lumotlar bazasi migratsiyalarini boshqarish uchun tayyorlangan.

## Modellar
1. User — foydalanuvchilar
2. Category — mahsulot kategoriyalari
3. Product — mahsulotlar

Har bir model uchun alohida Alembic migration fayli mavjud:
- `001_create_users.py`
- `002_create_categories.py`
- `003_create_products.py`

## 1. Muhitni tayyorlash

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Migratsiyalarni ishga tushirish

Loyiha papkasida:
```bash
alembic upgrade head
```

Migratsiyalar holatini ko'rish:
```bash
alembic current
alembic history
```

Oxirgi migratsiyani bekor qilish:
```bash
alembic downgrade -1
```

Bazani barcha migratsiyalardan orqaga qaytarish:
```bash
alembic downgrade base
```

## 3. API serverini ishga tushirish

```bash
uvicorn app.main:app --reload
```

Brauzerda:
- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs

## 4. Yangi migratsiya yaratish

Modelga o'zgartirish kiritgandan keyin:
```bash
alembic revision --autogenerate -m "migration tavsifi"
```
Alembic yaratgan faylni tekshirib, so'ng:
```bash
alembic upgrade head
```

Eslatma: `--autogenerate` uchun `alembic/env.py` ichidagi `target_metadata` model metadata'siga bog'langan.
