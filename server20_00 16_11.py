import asyncio

from aiohts import Server, CSA_AES_IV, CSA_AES_KEY


class Serv(Server):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chunks = ["0001", "0003", "0010", "0012", "00ff", "0000"]

    async def process_messages(self, con, msg):
        await super().process_messages(con, msg)
        if msg.check_type_key("20", "00"):
            omsg = await con.build_message(
                sender="0" * 8,
                receiver=msg.sender,
                number=await con.get_number(),
                link=msg.link,
                type="16",
                payload=["11"]
            )
            await con.write_message(omsg)
			
async def amain():
    server = Serv(aes_key=CSA_AES_KEY, aes_iv=CSA_AES_IV, port=7176, host='0')
    await server.start()


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(amain())
    loop.run_forever()


if name == '__main__':
    main()