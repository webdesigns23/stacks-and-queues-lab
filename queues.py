import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued {item} | Queue: {self.items}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued {removed} | Queue: {self.items}")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None
    
    def peek(self):
        if not self.is_empty():
            print(f"Front of queue: {self.items[0]}")
            return self.items[0]
        else:
            print("Queue is empty. No front item.")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):    
        if self.is_empty():
            print("Queue is empty. No winner can be selected.")
            return None

        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items.pop(winner_index) 
        print(f'Winner: {winner}, Queue: {self.items}')
        return winner

# Tests
q = Queue()
q.enqueue("Luna")
q.enqueue("Pew")
q.enqueue("Grumps")
q.enqueue("Bryan")

winner = q.select_and_announce_winner()
print(f"The winner is: {winner}")



		
