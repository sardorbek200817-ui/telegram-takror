import asyncio
from aiogram import Router ,Bot , types , Dispatcher
from aiogram.filters import Command

router = Router()  

# Router bu vois yoki message ekanligini farqlab beradi va boshqa boshqa narsalarni



# xoxlagan habar kelsa Xush kelibsiz degan yozuv chiqaradi

@router.message() # message() xoxlagan text uchun yani hohlagan text kelsa javob beradi
async def start(message:types.Message):
    await message.reply("Xush kelibsiz")


@router.message(Command("help"))
async def help1(message:types.Message):
    await message.reply("Sizga qanday yordam bera olaman") # aynan yozgan textni belgilab javob sifatida qaytaradi

    await message.answer(f"sizga yozgan habar: {message.text}") # answer hamma text uchun javob qaytaradi


# hamma kodlarni  royhatdan otkazib qoyishimiz >>>  main()

async def main():
    
    bot = Bot(token="8790435378:AAHbyRY_oQPAgEM-1YzLeuh7nNa1pGzrzqY")
    dp = Dispatcher()

    await dp.start_polling(bot)

    dp.include_routers(
        router
    )


# hamma async kodlarni birga ishlatib beradigan narsa

if __name__ == "__main__":
    asyncio.run(main())







































