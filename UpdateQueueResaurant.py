#ตัวอย่างการประยุกต์ใช้คิวในการจำลองการรอคิวร้านอาหาร จะเกิดความผิดพลาดในการทำงานกรณีใด จงอธิบาย และจะแก้ไข Code อย่างไรเพื่อแก้ไขปัญหาดังกล่าว
#Ans จะเกิดความผิดพลาดในกรณี
# 1. การพยายามนำข้อมูลออกจากคิวว่าง (dequeue) เมื่อคิวว่าง จะทำให้เกิดข้อผิดพลาดหรือพฤติกรรมที่ไม่พึงประสงค์
# 2. การดูข้อมูลตัวสุดท้ายหรือหน้าคิวในคิวว่าง (peek, peek_last)หากเรียก peek() หรือ peek_last() บนคิวว่าง จะเกิดข้อผิดพลาด IndexError จะถูกโยน เพราะไม่มีข้อมูลในลิสต์ให้เข้าถึงตำแหน่ง -1 หรือ 0
#แก้ไข Code
#Ans 1.เพิ่มการตรวจสอบสถานะคิวว่างในเมธอด serve_customer และ peek_last
# 2.ปรับปรุงเมธอดใน Queue ให้จัดการกรณีคิวว่าง
# 3.เพิ่มการแจ้งเตือนเมื่อคิวว่าง
#ตัวอย่างโค้ดเเก้ไข

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
        else:
            print("คิวว่าง ไม่สามารถ dequeue ได้")
            return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("คิวว่าง ไม่มีข้อมูลหน้าคิว")
            return None
    
    def peek_last(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("คิวว่าง ไม่มีข้อมูลตัวสุดท้าย")
            return None
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        """ล้างข้อมูลทั้งหมดในคิว"""
        self.items = []
        print("ล้างข้อมูลในคิวเรียบร้อย")
    
    def display(self):
        if self.is_empty():
            print("คิวว่าง")
        else:
            print(f"Queue: {self.items}")

class Restaurant:
    def __init__(self):
        self.waiting_queue = Queue()
        
    def add_customer(self, name):
        self.waiting_queue.enqueue(name)
        print(f"ลูกค้า {name} เข้าคิวที่ {self.waiting_queue.size()}")
        
    def serve_customer(self):
        customer = self.waiting_queue.dequeue()
        if customer is not None:
            print(f"กำลังเสิร์ฟลูกค้า: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def last_customer(self):
        customer = self.waiting_queue.peek_last()
        if customer is not None:
            print(f"ลูกค้าคนสุดท้ายในคิวคือ: {customer}")
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def clear_queue(self):
        self.waiting_queue.clear()
    
    def show_queue(self):
        print("สถานะคิวปัจจุบัน:")
        self.waiting_queue.display()
        print(f"จำนวนลูกค้าในคิว: {self.waiting_queue.size()}")

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    restaurant = Restaurant()

    # เพิ่มลูกค้าเข้าคิว
    restaurant.add_customer("สมชาย")
    restaurant.add_customer("สมหญิง")
    restaurant.add_customer("สมหวัง")

    # แสดงสถานะคิว
    restaurant.show_queue()

    # เสิร์ฟลูกค้า
    restaurant.serve_customer()
    restaurant.serve_customer()

    # ดูลูกค้าคนสุดท้ายในคิว
    restaurant.last_customer()

    # ล้างคิวทั้งหมด
    restaurant.clear_queue()

    # แสดงสถานะคิวหลังล้าง
    restaurant.show_queue()

    # พยายามเสิร์ฟลูกค้าเมื่อคิวว่าง
    restaurant.serve_customer()
