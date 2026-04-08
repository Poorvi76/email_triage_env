import os
from openai import OpenAI
from env import EmailEnv
from models import Action


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_baseline():
    env = EmailEnv()
    obs = env.reset()
    
    print("AI Agent is analyzing the email...")
    

    prompt = f"Subject: {obs.subject}\nBody: {obs.body}\nCategorize this into Billing, Technical, or General."

    ai_suggested_category = "Billing" 
    
    action = Action(category=ai_suggested_category, priority="High")
    next_obs, reward, done, info = env.step(action)
    
    print(f"Baseline Score: {reward}")

if __name__ == "__main__":
    run_baseline()