#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os
import re
import mirai
import traceback
import warnings


class JsonStorage(object):
    def __init__(self, file: os.PathLike = 'db.json'):

        # 打开数据库
        self.stream_io = open(file, 'a+', encoding='utf-8')
        try:
            self.stream_io.seek(0)
            self.db_data = json.load(self.stream_io)
        except json.JSONDecodeError:
            # 当出现问题需要重建（或新建）数据库时提醒用户
            warnings.warn('注意：已重置数据库')
            self.db_data = {}
            json.dump(self.db_data, self.stream_io)

    def update(self):
        # 清空已有的数据
        self.stream_io.seek(0)
        self.stream_io.truncate()

        # 然后导出内存中的数据
        json.dump(self.db_data, self.stream_io)

        self.stream_io.flush()

    def close(self):
        self.stream_io.close()


if __name__ == '__main__':
    bot = mirai.Mirai(
        qq=int(os.getenv('APP_QQ')),
        adapter=mirai.WebSocketAdapter(
            verify_key=os.getenv('APP_VERIFY_KEY'), host=os.getenv('APP_HOST'), port=int(os.getenv('APP_PORT'))
        )
    )

    db = JsonStorage()


    @bot.on(mirai.MessageEvent)
    async def message_command(event: mirai.MessageEvent):
        try:
            reg_match = re.match(r'^([a-zA-Z0-9_.-]+)=(.*)|\$([a-zA-Z0-9]+)$', str(event.message_chain))

            # 无操作（一般都是这种情况，所以放在第一位）
            if reg_match is None:
                return None

            # 写入
            elif reg_match.group(1) is not None:
                db.db_data[reg_match.group(1)] = reg_match.group(2)

                db.update()
                return bot.send(event, 'OK')

            # 读取
            elif reg_match.group(3) is not None:
                return bot.send(event, db.db_data[reg_match.group(3)])

        except:
            return bot.send(event, traceback.format_exc())


    try:
        bot.run()
    except KeyboardInterrupt:
        db.close()
