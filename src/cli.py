import os
import argparse

parser = argparse.ArgumentParser(description="Product Classifier CLI")
parser.add_argument('command', choices=['train', 'test', 'start'], help='Command to execute')
args = parser.parse_args()

if args.command == 'train':
    from train import train_model
    train_model()
elif args.command == 'test':
    from test import test_model
    test_model()
elif args.command == 'start':
    from api import app
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
else:
    print(f"Unknown command: {args.command}")
