# cicflowmeter
this tool to analysis packets and flow network .it is such as cicflowmete.

# 🛡️ cicflowp - Network Flow Feature Extractor

`cicflowp` هي أداة Python لاستخلاص ميزات تدفقات الشبكة (Flows) من ملفات PCAP. تم تصميمها لتستخدم في تحليل حركة الشبكة، دعم مشاريع الأمن السيبراني، وتجهيز بيانات لتدريب نماذج تعلم الآلة.

---

## 📦 محتويات المشروع

```
cicflowp/
├── main.py                  # نقطة التشغيل الرئيسية
├── requirements.txt         # المكتبات المطلوبة
├── config.py                # الإعدادات العامة
├── reader/
│   └── pcap_reader.py       # قراءة ملفات PCAP
├── flow/
│   ├── flow.py              # تمثيل كائن تدفق الشبكة
│   └── flow_builder.py      # بناء جلسات التدفق
├── features/
│   ├── *.py                 # وحدات استخراج الميزات (17 وحدة حالياً)
├── output/
│   └── writer.py            # إخراج النتائج إلى CSV
├── test_data/
│   └── example.pcap         # ملف تجريبي
└── output_files/
    └── flows.csv            # الميزات المستخرجة النهائية
```

---

## 🎯 الهدف

- تحويل ملفات PCAP إلى تمثيل منظم لتدفقات TCP/UDP.
- استخراج **79 ميزة** من كل تدفق.
- تخزين النتائج بصيغة CSV.
- تسهيل تدريب نماذج ML لاحقًا أو استخدامها لتحليل حركة الشبكة.

---

## ⚙️ كيفية التشغيل

```bash
python main.py --input test_data/example.pcap --output output_files/flows.csv
```

> تأكد من تعديل المسارات في `config.py` أو تمريرها كسطر أوامر إذا كانت الأداة تدعم ذلك.

---

## 🧠 الميزات المستخرجة

- طول الحزم، عدد الحزم في كلا الاتجاهين
- الزمن بين الحزم (IAT)
- إشارات TCP (SYN, ACK, etc)
- طول رؤوس الحزم
- حجم البيانات المرسلة والمستلمة
- معدل الإرسال، حجم القطاعات، النوافذ، النشاط والكمون

---

## 🔧 المتطلبات

- Python 3.8+
- مكتبات:
  - scapy
  - numpy
  - pandas
  - tqdm
  - أي مكتبات إضافية مدرجة في `requirements.txt`

---

## 🧪 حالة التطوير

✅ قراءة ملفات PCAP  
✅ بناء الجلسات  
✅ استخراج 79 ميزة  
🔜 دعم البيانات الحية (Live Capture)

---

## 👨‍💻 المطور

- **الاسم:** Mohammed Ammar Mohammed Noman  
- **المجال:** Cybersecurity & Network Traffic Analysis  
- **المشروع جزء من مادة:** IT Project Management

---

## 📜 الترخيص

MIT License
