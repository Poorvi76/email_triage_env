import pydantic
from models import Observation, Action, Reward

class EmailEnv:
    def __init__(self):
        
        self.tasks = [
            {"subject": "Refund Request", "body": "I want my money back for order #123", "category": "Billing"},
            {"subject": "Login Error", "body": "I cannot access my account, it shows error 404", "category": "Technical"},
            {"subject": "Urgent: Server Down", "body": "Our entire team can't work!", "category": "Technical"}
        ]
        self.current_step = 0

    def reset(self) -> Observation:
        self.current_step = 0
        task = self.tasks[self.current_step]
        return Observation(subject=task["subject"], body=task["body"], sender="user@example.com")

    def step(self, action: Action):
        correct_category = self.tasks[self.current_step]["category"]
        
        # Grading Logic (Simple Example)
        if action.category == correct_category:
            reward = 1.0
            done = True
        else:
            reward = 0.0
            done = False
            
        self.current_step += 1
        info = {"message": "Task processed"}
        
        # Next observation (agar tasks bache hain)
        obs = self.reset() if not done else None
        return obs, reward, done, info

    def state(self):
        return {"current_task_index": self.current_step}
    
if __name__ == "__main__":
  
    my_env = EmailEnv()
    
    print("--- Initializing Environment ---")
   
    obs = my_env.reset()
    print(f"Observation: {obs}")

    
    test_action = Action(category="Billing", priority="Medium")
    
    print("\n--- Taking Step ---")
    obs, reward, done, info = my_env.step(test_action)
    
    print(f"Reward received: {reward}")
    print(f"Is task done?: {done}")
    print(f"Info: {info}")