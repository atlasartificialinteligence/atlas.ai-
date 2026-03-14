#!/usr/bin/env python3
import random

GREETINGS = [
    "Hello, World!",          # English
    "Olá, Mundo!",            # Portuguese
    "¡Hola, Mundo!",          # Spanish
    "Bonjour, le monde !",    # French
    "Hallo, Welt!",           # German
]

for greeting in random.sample(GREETINGS, k=len(GREETINGS)):
    print(greeting)
