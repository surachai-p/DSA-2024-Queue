class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def peek_last(self):
        """ดูข้อมูลตัวสุดท้ายในคิวโดยไม่นำออก"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: {self.items}")
    
    def clear(self):
        """ล้างข้อมูลทั้งหมดในคิว"""
        self.items = []
        print("คิวถูกล้างเรียบร้อยแล้ว")

# ทดสอบ Queue พร้อมฟังก์ชัน peek_last()
q = Queue()

# เพิ่มข้อมูลลงในคิว
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # ควรได้ [1, 2, 3]

# ใช้ peek_last() เพื่อดูข้อมูลตัวสุดท้าย
last_item = q.peek_last()
print("ข้อมูลตัวสุดท้ายในคิว:", last_item)  # ควรได้ 3

# ยืนยันว่าคิวไม่เปลี่ยนแปลง
q.display()  # ควรได้ [1, 2, 3]
