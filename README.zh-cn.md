# CMAN -spider

## 这是什么？

CMAN-spider 是 CMAN 的一个子项目。CMAN-spider 用于从 Modrinth 下载 Mod 相关信息，并将其存储为 .mod 文件。

.mod 文件是 CMAN 用来查找 Mod 的索引。.mod文件可以帮助CMAN快速有效地处理mod之间的依赖关系，您还可以通过向CMAN添加其他非官方来源，将更多的mod载入CMAN。

## 谁会运行CMAN-spider？

CMAN-spider 由 CMAN 社区的志愿者运行，然后 CMAN-spider 将 .mod 文件上传到 GitHub 供 CMAN 使用。

## 开始

首先，克隆 CMAN-spider repo 到您的电脑。并确保安装了 python3.8

```bash
git clone https://github.com/Minecraft-CMAN/CMAN-spider.git
```

然后，用 poetry 安装需求。<u>如果没有安装 poetry，请使用 `pip install poetry` 安装</u>。

```bash
poetry install
```

然后用 `poetry run python main.py` 运行它。