# mirai-boring-env

一个使用python编写的有用，但非常无聊的东西

*本项目依赖[mirai](https://github.com/mamoe/mirai), [mirai-api-http](https://github.com/project-mirai/mirai-api-http)*
## 启动

```shell
# 克隆仓库
git clone https://github.com/Yang-qwq/mirai-boring-env.git
cd mirai-boring-env

# 设置虚拟环境（可选）
# 此步骤请根据你所在的平台灵活调整
python -m venv venv
./venv/Scripts/activate.ps1 

# 安装依赖
pip install -r requirements.txt

# 启动
python main.py
```
## 环境变量解释

- `APP_QQ` 指定mirai中使用机器人的qq号，若singleMode已开启，可填写任意整数
- `APP_VERIFY_KEY` 验证密钥，可在mirai-api-http中的setting.yml找到
- `APP_HOST` mirai-api-http所在的主机
- `APP_PORT` mirai-api-http使用的端口