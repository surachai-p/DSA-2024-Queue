
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("คิวว่าง ไม่สามารถเสิร์ฟลูกค้าได้.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek_first(self):
        if not self.is_empty():
            return self.items[0]
        return None


class HairSalonQueueSystem:
    def __init__(self):
        self.waiting_queue = Queue()

    def add_customer(self, name, service_type):
        customer_info = {"name" : name, "service_type" : service_type}
        self.waiting_queue.enqueue(customer_info)
        print(f"เพิ่มลูกค้า : {name} ({service_type})")

    def serve_customer(self):
        customer = self.waiting_queue.dequeue()
        if customer:
            print(f"เรียกลูกค้า : {customer['name']}")

    def show_queue(self):
        if self.waiting_queue.is_empty():
            print("คิวว่าง ไม่มีลูกค้ารอ")
        else:
            print("แสดงคิว : ")
            total_wait_time = 0
            for idx, customer in enumerate(self.waiting_queue.items, start=1):
            
                if customer['service_type'] == 'ตัดผม':
                    wait_time = 30
                elif customer['service_type'] == 'สระ':
                    wait_time = 20
                elif customer['service_type'] == 'ย้อมสี':
                    wait_time = 60
                total_wait_time += wait_time
                print(f"{idx}. {customer['name']} - {customer['service_type']} (รอประมาณ {total_wait_time} นาที)")

    def estimated_wait_time(self):
        if self.waiting_queue.is_empty():
            print("คิวว่าง ไม่มีลูกค้ารอ")
        else:
            total_wait_time = 0
            for customer in self.waiting_queue.items:
                
                if customer['service_type'] == 'ตัดผม':
                    total_wait_time += 30
                elif customer['service_type'] == 'สระ':
                    total_wait_time += 20
                elif customer['service_type'] == 'ย้อมสี':
                    total_wait_time += 60
            return total_wait_time


salon_system = HairSalonQueueSystem()

# แสดงข้อความต้อนรับ
print("=== ร้านตัดผมคุณหรีด ===")

# เพิ่มลูกค้าเข้าคิว
salon_system.add_customer("สมชาย", "ตัดผม")
salon_system.add_customer("สมหญิง", "ย้อมสี")

# แสดงคิวทั้งหมด
salon_system.show_queue()

# เรียกลูกค้าคนถัดไป
salon_system.serve_customer()

# แสดงคิวที่เหลือ
salon_system.show_queue()