import openenv
from env import EmailEnv

try:
    env = EmailEnv()
    obs = env.reset()
    print("✅ Reset works!")
    
    from models import Action
    test_action = Action(category="Billing", priority="Low")
    obs, reward, done, info = env.step(test_action)
    print(f"✅ Step works! Reward: {reward}")
    
    print("\nEnvironment is looking good for submission!")
except Exception as e:
    print(f"❌ Error: {e}")