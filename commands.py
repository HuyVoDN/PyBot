from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

RACIST_WORDS_N = os.getenv('RACIST_WORDS_N')
RACIST_WORDS_C = os.getenv('RACIST_WORDS_C')
@commands.command()
async def response(ctx):
    await ctx.send('Hello!')

@commands.command()
async def addition(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f'The addition is {result}')
    
@commands.command()
async def repeat(ctx, sentence: str, freq: int):
   
    for i in range(freq):
        if sentence.lower() in RACIST_WORDS_N:
            await ctx.send(sentence + ":baby_tone5:")
        elif sentence.lower() in RACIST_WORDS_C:
            await ctx.send(sentence + ":man_with_chinese_cap:")
        else:
            await ctx.send(sentence)
    