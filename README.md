# CMAN-spider

English  [简体中文](./README.zh-cn.md)

## What's this?

CMAN-spider is a sub-project of CMAN. CMAN-spider is used to download Mod-related information from Modrinth and store them as .mod files.

The .mod file is the index that CMAN uses to find mods. The .mod file can helps CMAN handle dependencies between mods quickly and efficiently, and you can also load more mods into CMAN by adding other unofficial sources into CMAN.

## Who will runs the CMAN-spider?

The CMAN-spider is run by volunteers in the CMAN community, and then CMAN-spider uploads the .mod file to GitHub for use by CMAN

## Getting Started

First, clone CMAN-spider repo to your computer. And make sure python3.8 is installed

```bash
git clone https://github.com/Minecraft-CMAN/CMAN-spider.git
```

Then, install requirements by poetry. <u>If you don't install poetry, use `pip install poetry` to install it</u>.

```bash
poetry install
```

And run it by `poetry run python main.py`.
