import pydantic
from fastapi import FastAPI
from models import Observation, Action
import uvicorn

app = FastAPI()

class EmailEnv:
    def __init__(self):
        self.tasks = [
            {"subject": "Refund Request", "body": "I want my money back for order #123", "category": "Billing"},
            {"subject": "Login Error", "body": "I cannot access my account, it shows error 404", "category": "Technical"},
            {"subject": "Urgent: Server Down", "body": "Our entire team can't work!", "category": "Technical"}
        ]
        self.current_step = 0

    def reset(self):
        self.current_step = 0
        task = self.tasks[self.current_step]
        # Format consistent rakha hai Meta ke liye
        return {
            "observation": {
                "subject": task["subject"],
                "body": task["body"],
                "sender": "user@example.com"
            },
            "info": {}
        }

    def step(self, action: Action):
        correct_category = self.tasks[self.current_step]["category"]
        if action.category == correct_category:
            reward = 1.0
            done = True
        else:
            reward = 0.0
            done = False
            
        self.current_step = (self.current_step + 1) % len(self.tasks)
        return {
            "observation": "Task processed",
            "reward": reward,
            "done": done,
            "info": {"message": "Action processed"}
        }

my_env = EmailEnv()

@app.post("/reset")
def reset_endpoint():
    return my_env.reset()

@app.post("/step")
def step_endpoint(action: Action):
    return my_env.step(action)

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
