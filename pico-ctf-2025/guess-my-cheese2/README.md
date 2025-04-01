## **HINT:**  
- "Cheese" được mã hóa bằng **SHA-256**.  
- Có thêm **salt** là **2 nibbles of hex-character**, tức là **1 byte**.  

---

## **Hướng giải:**  
1. **Mã hóa toàn bộ `cheese + salt`**.  
2. **Salt** có thể được thêm vào **bất kỳ vị trí nào trong "cheese"**.  
3. "Cheese" có thể **in thường hoặc in hoa**.  

---

### **Cách 1:**
```python
for line in cheese_list:
    line = line.strip()
    for s in string.printable:
        for i in range(len(line) + 1):
            text = line[:i] + s + line[i:]
            encrypt(text.encode())

            text = line[:i].lower() + s + line[i:].lower()
            encrypt(text.encode())

            text = line[:i].upper() + s + line[i:].upper()
            encrypt(text.encode())
```

❌ Nhược điểm: string.printable không đủ 256 giá trị có thể có của 1 byte, có thể không tìm được salt đúng.


### **Cách 2:**
```python
for line in cheese_list:
    line = line.encode()
    for s in range(256):
        for i in range(len(line) + 1):
            text = line[:i] + bytes([s]) + line[i:]
            encrypt(text)
            text = line[:i].lower() + bytes([s]) + line[i:].lower()
            encrypt(text)
            text = line[:i].upper() + bytes([s]) + line[i:].upper()
```
✅ Ưu điểm:
- Đủ 256 trường hợp của 1 byte salt.
- Không bị giới hạn bởi string.printable.

``` Flag: picoCTF{cHeEsY0f5cd2b5} ```