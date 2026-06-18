# ระบบติดตามการบ้าน (Homework Tracking System)

# 1. สร้างฐานข้อมูลการบ้านเก็บไว้ในรูปแบบ Dictionary
# กำหนดค่าเริ่มต้นว่ายังไม่ได้ทำอะไรเลย บลาๆ
homework_list = {
    "วิชาคอมพิวเตอร์": "ยังไม่ได้เริ่มทำอะไรเลย (ว่างอยู่ บลาๆ)",
    "วิชาคณิตศาสตร์": "ยังไม่ได้เริ่มทำอะไรเลย (ว่างอยู่ บลาๆ)",
    "วิชาภาษาอังกฤษ": "ยังไม่ได้เริ่มทำอะไรเลย (ว่างอยู่ บลาๆ)"
}

def show_homework():
    """ฟังก์ชันสำหรับดูสถานะการบ้านทั้งหมด"""
    print("\n==== รายงานสถานะการบ้านปัจจุบัน ====")
    for subject, status in homework_list.items():
        print(f"📚 {subject}: สถานะ -> {status}")
    print("=================================\n")

def update_status():
    """ฟังก์ชันสำหรับระบุหรือเปลี่ยนสถานะการบ้าน"""
    show_homework()
    subject_input = input("พิมพ์ชื่อวิชาที่ต้องการอัปเดตสถานะ: ")
    
    if subject_input in homework_list:
        new_status = input(f"ระบุสถานะใหม่ของ {subject_input} (เช่น กำลังทำ, เสร็จแล้ว): ")
        homework_list[subject_input] = new_status
        print(f"🎉 อัปเดตสถานะ {subject_input} สำเร็จแล้ว!")
    else:
        print("❌ ไม่พบวิชานี้ในระบบ กรุณาลองใหม่")

# --- ส่วนหลักของโปรแกรม (Menu) ---
while True:
    print("--- เมนูระบบติดตามการบ้าน ---")
    print("1. ดูสถานะการบ้านทั้งหมด")
    print("2. ระบุ/อัปเดตสถานะการบ้าน")
    print("3. ออกจากโปรแกรม")
    
    choice = input("เลือกเมนู (1/2/3): ")
    
    if choice == "1":
        show_homework()
    elif choice == "2":
        update_status()
    elif choice == "3":
        print("ปิดระบบแล้ว บ๊ายบายครับ! อย่าลืมเคลียร์การบ้านนะ")
        break
    else:
        print("พิมพ์เมนูไม่ถูกต้องจ้า ลองใหม่อีกทีนะ\n")